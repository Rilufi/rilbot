from auth import *
import fortune
import os

fortune = os.popen("fortune fortunes").read()
while len(fortune) > 280:
	fortune = os.popen("fortune fortunes").read()
api.update_status(fortune)

def main():
    account_name = 'boturitter'
    for tweet in tweepy.Cursor(api.user_timeline, id=account_name).items(1):
        try:
           tweet.favorite()
           tweet.retweet()
           print("Tweet Retweeted")
        except tweepy.TweepError as e:
           print(e.reason)
        except StopIteration:
           break
main()
