import tweepy
import os

#Ril

consumer_key = os.environ["CONSUMER_KEY_RIL"]
consumer_secret = os.environ["CONSUMER_SECRET_RIL"]
access_token = os.environ["ACCESS_TOKEN_RIL"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET_RIL"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Controls Twitter account
api = tweepy.API(auth, wait_on_rate_limit = True)


#Xame

consumer_key = os.environ["CONSUMER_KEY_XAME"]
consumer_secret = os.environ["CONSUMER_SECRET_XAME"]
access_token = os.environ["ACCESS_TOKEN_XAME"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET_XAME"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api_xame = tweepy.API(auth, wait_on_rate_limit = True)


#Uva

consumer_key = os.environ["CONSUMER_KEY_UVA"]
consumer_secret = os.environ["CONSUMER_SECRET_UVA"]
access_token = os.environ["ACCESS_TOKEN_UVA"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET_UVA"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Controls Twitter account
api_uva = tweepy.API(auth, wait_on_rate_limit = True)


#Mevu

consumer_key = os.environ["CONSUMER_KEY_MEVU"]
consumer_secret = os.environ["CONSUMER_SECRET_MEVU"]
access_token = os.environ["ACCESS_TOKEN_MEVU"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET_MEVU"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Controls Twitter account
api_mevu = tweepy.API(auth, wait_on_rate_limit = True)


#Zark

consumer_key = os.environ["CONSUMER_KEY_ZARK"]
consumer_secret = os.environ["CONSUMER_SECRET_ZARK"]
access_token = os.environ["ACCESS_TOKEN_ZARK"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET_ZARK"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Controls Twitter account
api_zark = tweepy.API(auth, wait_on_rate_limit = True)


#Lufi

consumer_key = os.environ["CONSUMER_KEY_LUFI"]
consumer_secret = os.environ["CONSUMER_SECRET_LUFI"]
access_token = os.environ["ACCESS_TOKEN_LUFI"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET_LUFI"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Controls Twitter account
api_lufi = tweepy.API(auth, wait_on_rate_limit = True)


#Woba

consumer_key = os.environ["CONSUMER_KEY_WOBA"]
consumer_secret = os.environ["CONSUMER_SECRET_WOBA"]
access_token = os.environ["ACCESS_TOKEN_WOBA"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET_WOBA"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Controls Twitter account
api_woba = tweepy.API(auth, wait_on_rate_limit = True)


#Majin

consumer_key = os.environ["CONSUMER_KEY_MAJ"]
consumer_secret = os.environ["CONSUMER_SECRET_MAJ"]
access_token = os.environ["ACCESS_TOKEN_MAJ"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET_MAJ"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Controls Twitter account
api_maj = tweepy.API(auth, wait_on_rate_limit = True)
