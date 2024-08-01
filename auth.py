import tweepy
import os


#Xame

api_xame = tweepy.Client(
    consumer_key = os.environ.get("CONSUMER_KEY_XAME"),
    consumer_secret = os.environ.get("CONSUMER_SECRET_XAME"),
    access_token = os.environ.get("ACCESS_TOKEN_XAME"),
    access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET_XAME")
)


#Uva

api_uva = tweepy.Client(
    consumer_key = os.environ.get("CONSUMER_KEY_UVA"),
    consumer_secret = os.environ.get("CONSUMER_SECRET_UVA"),
    access_token = os.environ.get("ACCESS_TOKEN_UVA"),
    access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET_UVA")
)


#Mevu

api_mevu = tweepy.Client(
    consumer_key = os.environ.get("CONSUMER_KEY_MEVU"),
    consumer_secret = os.environ.get("CONSUMER_SECRET_MEVU"),
    access_token = os.environ.get("ACCESS_TOKEN_MEVU"),
    access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET_MEVU")
)


#Zark

api_zark = tweepy.Client(
    consumer_key = os.environ.get("CONSUMER_KEY_ZARK"),
    consumer_secret = os.environ.get("CONSUMER_SECRET_ZARK"),
    access_token = os.environ.get("ACCESS_TOKEN_ZARK"),
    access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET_ZARK")
)


#Lufi

api_lufi = tweepy.Client(
    consumer_key = os.environ.get("CONSUMER_KEY_LUFI"),
    consumer_secret = os.environ.get("CONSUMER_SECRET_LUFI"),
    access_token = os.environ.get("ACCESS_TOKEN_LUFI"),
    access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET_LUFI")
)



#Majin

api_maj = tweepy.Client(
    consumer_key = os.environ.get("CONSUMER_KEY_MAJ"),
    consumer_secret = os.environ.get("CONSUMER_SECRET_MAJ"),
    access_token = os.environ.get("ACCESS_TOKEN_MAJ"),
    access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET_MAJ")
)



#Zelander

api_zeld = tweepy.Client(
    consumer_key = os.environ.get("CONSUMER_KEY_ZELD"),
    consumer_secret = os.environ.get("CONSUMER_SECRET_ZELD"),
    access_token = os.environ.get("ACCESS_TOKEN_ZELD"),
    access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET_ZELD")
)

