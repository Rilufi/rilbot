# Run: py twitter_bot.py
from auth import api
from datetime import datetime
from twitter_winner import winner

# Create class instance
win = winner()

day = datetime.today().day

# Run script
if day in [5, 9, 15, 23, 30]:
  print("Mevuxa is not home today.")
  pass
else:
  win.favorite_follow_retweet()

print(win.sort_file('twitterFilter.txt') + '\n')
