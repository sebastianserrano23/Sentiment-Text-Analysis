from textblob import TextBlob

with open('my_text.txt', 'r') as f:
    text = f.read()


blob = TextBlob(text)
sentiment = blob.sentiment.polarity(-1 or 1)

print(sentiment)
