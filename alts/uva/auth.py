import tweepy
import os

#Uva

api= tweepy.Client(

consumer_key = os.environ.get("CONSUMER_KEY_UVA"),
consumer_secret = os.environ.get("CONSUMER_SECRET_UVA"),
access_token = os.environ.get("ACCESS_TOKEN_UVA"),
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET_UVA")
)
