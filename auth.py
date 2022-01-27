import tweepy
import os

#Rilufi

consumer_key = os.environ["CONSUMER_KEY_RIL"]
consumer_secret = os.environ["CONSUMER_SECRET_RIL"]
access_token = os.environ["ACCESS_TOKEN_RIL"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET_RIL"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Controls Twitter account
api = tweepy.API(auth, wait_on_rate_limit = True)
