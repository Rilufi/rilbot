# Run: py twitter_bot.py
from auth import api
from datetime import datetime
from twitter_winner import winner

# Create class instance
win = winner()

day = datetime.today().day

# Run script
if day in [4, 8, 11, 18, 25]:
  print("Rilufix not today, Satan.")
  pass
else:
  win.favorite_follow_retweet()

print(win.sort_file('twitterFilter.txt') + '\n')
