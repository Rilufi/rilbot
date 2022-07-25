# Run: py twitter_bot.py
from auth import api
from datetime import datetime
from twitter_winner import winner
from twitter_unfollow import unfollow

# Create class instance
win = winner()
unfollow = unfollow()

day = datetime.today().day

# Run script
if day in [2, 11, 16, 20, 27]:
  print("Zarknall is nowhere to be found.")
  unfollow.unfollow()
else:
  win.favorite_follow_retweet()

print(win.sort_file('twitterFilter.txt') + '\n')
