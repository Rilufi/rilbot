import tweepy
import os

#Xamexavu

consumer_key = os.environ["CONSUMER_KEY_XAME"]
consumer_secret = os.environ["CONSUMER_SECRET_XAME"]
access_token = os.environ["ACCESS_TOKEN_XAME"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET_XAME"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True, timeout = 1000)
