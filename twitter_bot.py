# Run: py twitter_bot.py
from auth import api
from datetime import datetime
from twitter_clean_timeline import cleanTimeline
#from twitter_unfollow import unfollow
from twitter_winner import winner
import os

# Create class instance
win = winner()
#unfollow = unfollow()
clean_timeline = cleanTimeline()

os.system('cls')

day = datetime.today().day

# Call fortune
COMMAND = "fortune"
fortune = os.popen(COMMAND).read()
#while len(fortune) > 280:
#	fortune = os.popen(COMMAND).read()

# Run script
try:
	if api.me().friends_count > 3000:
	    #unfollow.unfollow()
	    api.update_status(fortune)
	elif api.me().favourites_count > 6000 or api.me().statuses_count > 6000:
	    clean_timeline.unfavorite_unretweet()
	    api.update_status(fortune)
	else:
	    win.favorite_follow_retweet()
	    api.update_status(fortune)
	print(win.sort_file('twitterFilter.txt') + '\n')
except:
	api.update_status(fortune)
