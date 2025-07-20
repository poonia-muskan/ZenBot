<img width="1919" height="916" alt="Screenshot 2025-07-20 101539" src="https://github.com/user-attachments/assets/31d2a066-5a91-478b-a871-b3b78b246590" /><img width="1919" height="916" alt="Screenshot 2025-07-20 101539" src="https://github.com/user-attachments/assets/af81f885-6561-4b59-9562-bca8c328c886" />🧘‍♀️ ZenBot – Your AI therapist
🧠 Overview
ZenBot is a lightweight, interactive web app designed to help users navigate mental wellness with calmness and clarity. It offers daily affirmations, mood tracking, mindfulness journaling, and soft bot interactions—creating a safe digital space for reflection and healing. ZenBot isn’t a therapist, but it is that one chill friend who always listens, never judges, and gently nudges you towards better vibes 🌿💬

---

🎯 Features
💬 Chat with ZenBot
 - A mindful chatbot that responds to your mood, feelings, or random rants
 - Provides calming messages, suggestions, and affirmations

📆 Mood Tracker
 - Log how you're feeling every day
 - See patterns in your emotional journey over time

📓 Journaling Corner
 - Write your thoughts, gratitude notes, or reflections
 - Stored locally for privacy & comfort

🌈 Daily Affirmations
 - Get a new positive affirmation each time you visit
 - Feel empowered and mentally recharged 💖

🌑 Dark Mode UI
 - Relaxing aesthetic perfect for late-night vent sessions
 - Simple, soothing design that doesn’t overwhelm

---

💻 Tech Stack
🧠 Backend & Framework
 - Python 3 – Core language
 - Flask – Web framework used to build the entire app
 - Flask-Login – User session management
 - Flask-Dance – Google OAuth2 login integration
 - Flask-Mail – Email verification & password recovery
 - Flask-Migrate – Database migration support
 - Flask SQLAlchemy – ORM for handling database models

🗃️ Database
 - Database: SQLite for development; easily switchable to PostgreSQL using SQLAlchemy
 - Models like User, MoodLog, Message, Conversation, DiaryEntry etc.

📊 Sentiment Analysis & NLP
 - TextBlob – To analyze user sentiment from journal/chat input
 - Custom keyword-based training for mood detection (train_keywords)

🎨 Frontend
 - HTML + Embedded CSS – UI structure & styling (Dark Mode ✨)
 - JavaScript – For client-side interactivity
 - Jinja2 – Template rendering with Flask

🔐 Security
 - Werkzeug – For password hashing & verification
 - itsdangerous – For secure token generation (e.g., email verification)

🌍 Environment & Config
 - python-dotenv – Load environment variables securely
 - Logging – For error tracking and monitoring

🚀 Deployment
 - Render –> Deployed your app live using Render hosting

---

📸 Screenshots
<img width="1919" height="916" alt="Screenshot 2025-07-20 101539" src="https://github.com/user-attachments/assets/da11bbc0-5533-4c55-83d0-d02e4ce4a2c9" />
<img width="1919" height="909" alt="Screenshot 2025-07-20 101554" src="https://github.com/user-attachments/assets/1c00830d-7427-4b5e-9fa7-b1e2e6a14fb2" />
<img width="1919" height="908" alt="Screenshot 2025-07-20 101649" src="https://github.com/user-attachments/assets/6a884f09-42e8-4347-8807-08002fa6e874" />
<img width="1919" height="910" alt="Screenshot 2025-07-20 101814" src="https://github.com/user-attachments/assets/1b4d475c-293d-4c14-a08b-c8fa0b4ee4d8" />
<img width="1919" height="909" alt="Screenshot 2025-07-20 101833" src="https://github.com/user-attachments/assets/19086a9c-b57c-4093-94de-9fd1b52d1643" />

---

🚀 Live Demo
- Link 1 -> 🔗 [ZenBot Web App](https://zenbot-3mjb.onrender.com)
- Link 2 -> 🔗 [ZenBot Web App](https://zenbot-56x6.onrender.com)

---

🫶 Inspiration
ZenBot was born out of a simple idea: mental wellness should be accessible, gentle, and judgment-free. With increasing stress, burnout, and emotional overload in Gen Z and beyond, ZenBot creates a small digital sanctuary for anyone who just wants to breathe and be.

---

📂 Run Locally

git clone https://github.com/poonia-muskan/ZenBot.git
cd ZenBot
pip install -r requirements.txt
python app.py
