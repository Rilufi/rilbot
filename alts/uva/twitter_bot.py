# Run: py twitter_bot.py
from auth import api
from datetime import datetime
from twitter_winner import winner

# Create class instance
win = winner()

day = datetime.today().day

# Run script
if day in [1, 7, 14, 21, 28]
  print("Uvaxemax is on vacation.")
  pass
else:
  win.favorite_follow_retweet()

print(win.sort_file('twitterFilter.txt') + '\n')
