from auth import api
import fortune
import os

fortune = os.popen("fortune fortunes").read()
while len(fortune) > 280:
	fortune = os.popen("fortune fortunes").read()
api.update_status(fortune)

tweets = api.user_timeline(screen_name="boturitter", count=1, exclude_replies = True)
for tweet in tweets:
	try:
		tweet.favorite()
		tweet.retweet()
	except:
		pass
