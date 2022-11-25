import tweepy
import os

#Mevu

consumer_key = os.environ.get("CONSUMER_KEY_MEVU")
consumer_secret = os.environ.get("CONSUMER_SECRET_MEVU")
access_token = os.environ.get("ACCESS_TOKEN_MEVU")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET_MEVU")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Controls Twitter account
api = tweepy.API(auth, wait_on_rate_limit = True)
