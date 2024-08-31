import pandas as pd
import re
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns
data = {
    'timestamp': ['2024-08-25', '2024-08-26', '2024-08-26', '2024-08-27', '2024-08-27'],
    'text': [
        "I love this brand, they have amazing products!",
        "Terrible customer service, I'm so disappointed.",
        "Great experience with their latest product launch.",
        "I'm neutral about this, nothing special.",
        "Worst purchase ever! Never buying from them again."
    ]
}
df = pd.DataFrame(data)
def clean_text(text):
    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)
    text = re.sub(r'\@\w+|\#', '', text)
    text = re.sub(r"[^A-Za-z0-9\s]", '', text)
    text = text.lower()
    return text

df['cleaned_text'] = df['text'].apply(clean_text)
def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

df['sentiment'] = df['cleaned_text'].apply(get_sentiment)
plt.figure(figsize=(8, 6))
sns.countplot(x='sentiment', data=df, palette='coolwarm')
plt.title('Sentiment Distribution')
plt.show()
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['date'] = df['timestamp'].dt.date
sentiment_over_time = df.groupby(['date', 'sentiment']).size().unstack().fillna(0)

sentiment_over_time.plot(kind='line', figsize=(10, 6), marker='o')
plt.title('Sentiment Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Posts')
plt.legend(title='Sentiment')
plt.show()
