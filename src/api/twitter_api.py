import tweepy

def create_api():
    consumer_key = 'TU_CONSUMER_KEY'
    consumer_secret = 'TU_CONSUMER_SECRET'
    access_token = 'TU_ACCESS_TOKEN'
    access_token_secret = 'TU_ACCESS_TOKEN_SECRET'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)
