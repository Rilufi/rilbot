import tweepy
import os

# Majin

consumer_key = os.environ.get("CONSUMER_KEY_MAJ")
consumer_secret = os.environ.get("CONSUMER_SECRET_MAJ")
access_token = os.environ.get("ACCESS_TOKEN_MAJ")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET_MAJ")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit = True)
