from dotenv import load_dotenv
load_dotenv()

import os
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_dance.contrib.google import make_google_blueprint, google
from chatbot.response_gen import get_response
from models.db import db
from models.user import User
from models.mood_log import MoodLog
from models.message import Message
from models.conversation import Conversation
from flask_mail import Mail, Message as MailMessage
import logging
from itsdangerous import URLSafeTimedSerializer
from chatbot.sentiment import analyze_sentiment, train_keywords
from flask_migrate import Migrate
from models.diary import DiaryEntry
from textblob import TextBlob

def mood_to_score(text):
    if not text:
        return 3  
    
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.5:
        return 5
    elif polarity > 0.2:
        return 4
    elif polarity > -0.2:
        return 3
    elif polarity > -0.5:
        return 2
    else:
        return 1

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
app.secret_key = "zenai_secret_key"
serializer = URLSafeTimedSerializer(app.secret_key)

# Email Configuration
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.getenv("EMAIL_USER") 
app.config["MAIL_PASSWORD"] = os.getenv("EMAIL_PASS") 

mail = Mail(app)

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'database', 'db.sqlite3')
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

# Google OAuth Setup
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
google_bp = make_google_blueprint(
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    redirect_url="/google/authorized",
    scope=[
        "openid",
        "https://www.googleapis.com/auth/userinfo.email",
        "https://www.googleapis.com/auth/userinfo.profile"
    ]
)
app.register_blueprint(google_bp, url_prefix="/login")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if User.query.filter_by(email=email).first():
            flash("User already exists. Try logging in.", "error")
            return redirect(url_for("register"))
        
        hashed_pw = generate_password_hash(password)
        new_user = User(email=email, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("dashboard"))
    return render_template("layout.html", register=True)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("dashboard"))
        else:
         flash("Invalid email or password.", "error")
    return render_template("login.html", register=False)

@app.route("/forgot_password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        email = request.form["email"]
        user = User.query.filter_by(email=email).first()

        if user:
            token = serializer.dumps(email, salt='password-reset-salt')
            reset_link = url_for('reset_password', token=token, _external=True)

            subject = "ZenBot Password Reset Request"
            msg = MailMessage(subject, sender=os.getenv("EMAIL_USER"), recipients=[email])
            msg.body = f"Hi there!\n\nTo reset your ZenBot password, click the link below:\n\n{reset_link}\n\nIf you didn’t request this, ignore it."

            mail.send(msg)

            flash("Reset link sent to your email. 📬", "success")
            return render_template("login.html")
        else:
            flash("No user found with that email you entered to reset password 😓", "error")
            return render_template("login.html")

    return render_template("forgot_password.html")

@app.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_password(token):
    try:
        email = serializer.loads(token, salt='password-reset-salt', max_age=3600)
    except Exception as e:
        flash("The reset link is invalid or expired.", "error")
        return redirect(url_for("login"))

    if request.method == "POST":
        new_password = request.form["password"]
        user = User.query.filter_by(email=email).first()
        if user:
            user.password = generate_password_hash(new_password)
            db.session.commit()
            flash("Password updated successfully! 🎉", "success")
            return redirect(url_for("login"))
        else:
            flash("User not found.", "error")

    return render_template("reset_password.html", token=token)

@app.route("/google/authorized")
def google_authorized():
    if not google.authorized:
        flash("Google login failed.", "error")
        return redirect(url_for("login"))

    resp = google.get("https://www.googleapis.com/oauth2/v2/userinfo")
    if not resp.ok:
        flash("Failed to fetch user info.", "error")
        return redirect(url_for("login"))

    user_info = resp.json()
    email = user_info["email"]
    profile_pic = user_info.get("picture")
    name = user_info.get("name", email)

    user = User.query.filter_by(email=email).first()
    if not user:
        user = User(email=email, password=generate_password_hash("google-auth"))
        db.session.add(user)
        db.session.commit()

    login_user(user)

    session["profile_pic"] = profile_pic
    session["name"] = name
    return redirect(url_for("dashboard"))

@app.route("/dashboard")
@login_required
def dashboard():
    convo_id = request.args.get("convo_id")
    current_convo = None
    if convo_id:
        current_convo = Conversation.query.get(int(convo_id))
    else:
        current_convo = Conversation.query.filter_by(user_id=current_user.id)\
            .order_by(Conversation.created_at.desc()).first()

    messages = []
    if current_convo:
        messages = Message.query.filter_by(conversation_id=current_convo.id).order_by(Message.timestamp).all()

    all_convos = Conversation.query.filter_by(user_id=current_user.id).order_by(Conversation.created_at.desc()).all()

    return render_template(
        "dashboard.html",
        name=session.get("name", current_user.email),
        profile_pic=session.get("profile_pic"),
        messages=messages,
        conversations=all_convos,
        current_convo=current_convo
    )

@app.route("/conversation/<int:convo_id>")
@login_required
def view_conversation(convo_id):
    conversation = Conversation.query.get_or_404(convo_id)
    if conversation.user_id != current_user.id:
        flash("Access denied.", "error")
        return redirect(url_for("dashboard"))

    messages = Message.query.filter_by(conversation_id=convo_id).order_by(Message.timestamp).all()
    all_convos = Conversation.query.filter_by(user_id=current_user.id).order_by(Conversation.created_at.desc()).all()

    return render_template(
        "dashboard.html",
        name=session.get("name", current_user.email),
        profile_pic=session.get("profile_pic"),
        messages=messages,
        conversations=all_convos,
        current_convo=conversation
    )

@app.route("/chat", methods=["POST"])
@login_required
def chat():
    if request.is_json:
        data = request.get_json()
        user_input = data.get("mood")
        convo_id = data.get("conversation_id")
        start_new = data.get("start_new")  
    else:
        user_input = request.form.get("mood")
        convo_id = request.form.get("conversation_id")
        start_new = request.form.get("start_new")

    if start_new == "true" or not convo_id:
        conversation = Conversation(user_id=current_user.id)
        db.session.add(conversation)
        db.session.commit()
    else:
        conversation = Conversation.query.get(int(convo_id))

    response = None

    if user_input and user_input.strip():
        response = get_response(user_input)

        sentiment = analyze_sentiment(user_input)
        score = mood_to_score(user_input)

        keywords_by_sentiment = train_keywords(current_user.id)

        if not response or response.strip().lower() == "i'm still learning":
            logging.debug(f"Fallback triggered for user {current_user.id}: {user_input}")
            matched_sentiment = None
            user_words = user_input.lower().split()

            for sentiment_label, word_list in keywords_by_sentiment.items():
                if any(word in word_list for word in user_words):
                    matched_sentiment = sentiment_label
                    break

            if matched_sentiment == "positive":
                response = "That sounds lovely 💫 I'm happy you're feeling that way!"
            elif matched_sentiment == "negative":
                response = "Seems like you're feeling low 😢 I'm here for you, always. 🫂"
            elif matched_sentiment == "neutral":
                response = "Noted! I'm all ears if you want to talk more 🪷"
            else:
                response = "I'm listening 🌙 Tell me more, love."

        msg = Message(
            user_input=user_input,
            bot_response=response,
            user_id=current_user.id,
            conversation_id=conversation.id
        )
        db.session.add(msg)

        mood_log = MoodLog(
            user_id=current_user.id,
            mood=user_input,
            score=score,
            sentiment=sentiment
        )
        db.session.add(mood_log)
        db.session.commit()

    if request.is_json:
        return jsonify({
            "reply": response,
            "conversation_id": conversation.id
        })

    messages = Message.query.filter_by(conversation_id=conversation.id).order_by(Message.timestamp).all()
    all_convos = Conversation.query.filter_by(user_id=current_user.id).order_by(Conversation.created_at.desc()).all()

    return render_template(
        "dashboard.html",
        name=session.get("name", current_user.email),
        profile_pic=session.get("profile_pic"),
        response=response,
        messages=messages,
        conversations=all_convos,
        current_convo=conversation
    )

@app.route("/mood_data")
@login_required
def mood_data():
    logs = MoodLog.query.filter_by(user_id=current_user.id).all()
    data = {}

    for log in logs:
        date_str = log.timestamp.date().isoformat()
        mood_entry = {
            "score": log.score, 
            "message": log.mood  
        }
        data.setdefault(date_str, []).append(mood_entry)

    return jsonify(data)

@app.route("/delete_convo/<int:convo_id>", methods=["POST"])
@login_required
def delete_convo(convo_id):
    convo = Conversation.query.filter_by(id=convo_id, user_id=current_user.id).first()
    if convo:
        db.session.delete(convo)
        db.session.commit()
    return redirect(url_for("dashboard"))

@app.route("/delete_all_convos", methods=["POST"])
@login_required
def delete_all_convos():
    all_convos = Conversation.query.filter_by(user_id=current_user.id).all()
    for convo in all_convos:
       db.session.delete(convo)
    db.session.commit()
    return redirect(url_for("dashboard"))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))

@app.route("/me")
def me():
    return f"Logged in: {current_user.is_authenticated} | Email: {current_user.email if current_user.is_authenticated else 'N/A'}"

@app.route("/get_response", methods=["POST"])
def get_response_route():
    data = request.get_json()
    user_message = data.get("message", "")
    bot_reply = get_response(user_message)
    return jsonify({"reply": bot_reply})

@app.route('/delete_entry/<int:entry_id>', methods=['POST'])
@login_required
def delete_entry(entry_id):
    entry = DiaryEntry.query.get(entry_id)
    if entry and entry.user_id == current_user.id:
        db.session.delete(entry)
        db.session.commit()
    return redirect(url_for('diary'))

@app.route('/update_entry/<int:entry_id>', methods=['POST'])
def update_entry(entry_id):
    updated_content = request.form.get("updated_content")
    if updated_content:
        entry = DiaryEntry.query.get_or_404(entry_id)
        entry.content = updated_content
        db.session.commit()
    return redirect(url_for('diary'))

@app.route("/diary", methods=["GET", "POST"])
@login_required
def diary():
    user = current_user  

    if request.method == "POST":
        content = request.form.get("entry", "").strip()
        if content:
            new_entry = DiaryEntry(user_id=user.id, content=content)
            db.session.add(new_entry)
            db.session.commit()
            flash("Entry saved 📝", "success")
            return redirect(url_for("diary"))
        else:
            flash("Entry cannot be empty 😅", "danger")
            return redirect(url_for("diary"))

    entries = DiaryEntry.query.filter_by(user_id=user.id).order_by(DiaryEntry.timestamp.desc()).all()

    return render_template(
        "diary.html",
        entries=entries,
        name=session.get("name", user.email),
        profile_pic=session.get("profile_pic"),
    )

    entries = DiaryEntry.query.filter_by(user_id=user.id).order_by(DiaryEntry.timestamp.desc()).all()
if __name__ == "__main__":
    app.run(debug=True)