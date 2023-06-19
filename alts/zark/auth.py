import tweepy
import os

#Zark

api = tweppy.Client(
consumer_key = os.environ.get("CONSUMER_KEY_ZARK"),
consumer_secret = os.environ.get("CONSUMER_SECRET_ZARK"),
access_token = os.environ.get("ACCESS_TOKEN_ZARK"),
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET_ZARK")
)
