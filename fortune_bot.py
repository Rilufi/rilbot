from auth import api_xame
import fortune
import os

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
