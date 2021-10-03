import tweepy
from random import randint
from auth import api

def main():
    search = ("Astronomy Picture of the Day")
     
    numberofTweets = 1
    for tweet in tweepy.Cursor(api.search, search).items(numberofTweets):
        try:
            tweet.retweet()
            print("Tweet Retweeted")
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
main()