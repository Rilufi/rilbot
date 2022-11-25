import tweepy
import os

#Uva

consumer_key = os.environ.get("CONSUMER_KEY_UVA")
consumer_secret = os.environ.get("CONSUMER_SECRET_UVA")
access_token = os.environ.get("ACCESS_TOKEN_UVA")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET_UVA")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Controls Twitter account
api = tweepy.API(auth, wait_on_rate_limit = True)
