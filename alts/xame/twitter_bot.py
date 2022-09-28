# Run: py twitter_bot.py
from auth import api
from datetime import datetime
from twitter_winner import winner
from twitter_unfollow import unfollow
from xame import rtquery

# Create class instance
win = winner()
unfollow = unfollow()
rt = rtquery()

day = datetime.today().day

# Run script
if day in [3, 10, 17, 22, 26]:
  print("Xamexavu is meditating today.")
  rt.rtquery()
#  unfollow.unfollow()
else:
  win.favorite_follow_retweet()

print(win.sort_file('twitterFilter.txt') + '\n')
