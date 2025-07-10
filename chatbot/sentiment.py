from textblob import TextBlob
from models.mood_log import MoodLog 
def analyze_sentiment(text):
    """
    Analyze sentiment of the text using TextBlob.
    Returns: 'positive', 'neutral', or 'negative'
    """
    if not text:
        return "neutral"

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"
def train_keywords(user_id):
    keywords_by_sentiment = {
        "positive": set(),
        "neutral": set(),
        "negative": set()
    }

    logs = MoodLog.query.filter_by(user_id=user_id).all()

    for log in logs:
        words = log.mood.lower().split()
        for word in words:
            keywords_by_sentiment[log.sentiment].add(word)

    return {k: list(v) for k, v in keywords_by_sentiment.items()}