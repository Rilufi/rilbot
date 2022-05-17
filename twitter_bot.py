# Run: py twitter_bot.py
from auth import api
from datetime import datetime
from twitter_clean_timeline import cleanTimeline
from twitter_unfollow import unfollow
from twitter_winner import winner

# Create class instance
win = winner()
unfollow = unfollow()
clean_timeline = cleanTimeline()

day = datetime.today().day

# Run script
if day in [4, 8, 11, 18, 25]:
  print("Rilufix not today, Satan")
  pass
else:
  win.favorite_follow_retweet()

print(win.sort_file('twitterFilter.txt') + '\n')
