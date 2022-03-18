import tweepy
import os

#Zarknall


consumer_key = os.environ["CONSUMER_KEY_ZARK"]
consumer_secret = os.environ["CONSUMER_SECRET_ZARK"]
access_token = os.environ["ACCESS_TOKEN_ZARK"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET_ZARK"]


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Controls Twitter account
api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify=True) 