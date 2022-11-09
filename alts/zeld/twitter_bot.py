# Run: py twitter_bot.py
from auth import api
from datetime import datetime
from twitter_winner import winner
from zeld import rtquery

# Create class instance
win = winner()
rt = rtquery()

day = datetime.today().day

# Run script
if day in [2, 6, 11, 16, 26]:
  print("Zelda doesn't even care about Link.")
  rt.rtquery()
else:
  win.favorite_follow_retweet()

print(win.sort_file('twitterFilter.txt') + '\n')
