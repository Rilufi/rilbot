import tweepy
from auth import api

def main():
    search = ("Astronomy Picture of the Day")
     
    for tweet in tweepy.Cursor(api.search, search).items(1):
        try:
            tweet.retweet()
            print("Tweet Retweeted")
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
main()
