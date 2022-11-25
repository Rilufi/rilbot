import tweepy
import os


#Xame

consumer_key = os.environ.get("CONSUMER_KEY_XAME")
consumer_secret = os.environ.get("CONSUMER_SECRET_XAME")
access_token = os.environ.get("ACCESS_TOKEN_XAME")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET_XAME")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit = True)
