from datetime import datetime
from models.db import db

class MoodLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    mood = db.Column(db.String(100), nullable=False)  
    score = db.Column(db.Integer, nullable=False)     
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    sentiment = db.Column(db.String(20))
    user = db.relationship('User', backref='moods')