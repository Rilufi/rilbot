import tweepy
import os

#Wobafab

consumer_key = os.environ["CONSUMER_KEY_WOBA"]
consumer_secret = os.environ["CONSUMER_SECRET_WOBA"]
access_token = os.environ["ACCESS_TOKEN_WOBA"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET_WOBA"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit = True)
