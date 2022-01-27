import tweepy
import fortune
import os


consumer_key = os.environ["CONSUMER_KEY"]
consumer_secret = os.environ["CONSUMER_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Controls Twitter account
api_xame = tweepy.API(auth, wait_on_rate_limit = True)


fortune = os.popen("fortune fortunes").read()
while len(fortune) > 280:
	fortune = os.popen("fortune fortunes").read()
api_xame.update_status(fortune)

tweets = api_xame.user_timeline(screen_name="boturitter", count=1, exclude_replies = True)
for tweet in tweets:
	try:
		tweet.favorite()
		tweet.retweet()
	except:
		pass
