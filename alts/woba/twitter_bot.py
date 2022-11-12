# Run: py twitter_bot.py
from auth import api
from datetime import datetime
from twitter_winner import winner
from woba import rtquery

# Create class instance
win = winner()
rt = rtquery()
day = datetime.today().day

# Run script
if day in [2, 7, 12, 17, 22, 27]:
  print("Wobafab is training for a wrestling tournament.")
  rt.rtquery()
else:
  win.favorite_follow_retweet()

print(win.sort_file('twitterFilter.txt') + '\n')
