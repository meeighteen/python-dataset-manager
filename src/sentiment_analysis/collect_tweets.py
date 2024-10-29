import tweepy
import pandas as pd
from api import create_api

def collect_tweets(keyword, count=100):
    api = create_api()
    tweets = tweepy.Cursor(api.search_tweets, q=keyword, lang='es', tweet_mode='extended').items(count)
    
    data = []
    for tweet in tweets:
        data.append([tweet.created_at, tweet.full_text])
    
    return pd.DataFrame(data, columns=['Date', 'Tweet'])

# Ejemplo de uso
if __name__ == '__main__':
    df_tweets = collect_tweets('Python', count=100)
    df_tweets.to_csv('tweets.csv', index=False)
