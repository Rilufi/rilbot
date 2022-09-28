# Run: py twitter_bot.py
from auth import api
from datetime import datetime
from twitter_winner import winner
from twitter_unfollow import unfollow
from woba import rtquery

# Create class instance
win = winner()
unfollow = unfollow()
rt = rtquery()

day = datetime.today().day

# Run script
if day in [1, 10, 15, 20, 25]:
  print("Wobafab is training for a wrestling tournament.")
  rt.rtquery()
#  unfollow.unfollow()
else:
  win.favorite_follow_retweet()

print(win.sort_file('twitterFilter.txt') + '\n')
