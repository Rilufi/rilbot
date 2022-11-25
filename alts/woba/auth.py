import tweepy
import os


#Woba

consumer_key = os.environ.get("CONSUMER_KEY_WOBA")
consumer_secret = os.environ.get("CONSUMER_SECRET_WOBA")
access_token = os.environ.get("ACCESS_TOKEN_WOBA")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET_WOBA")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit = True)
