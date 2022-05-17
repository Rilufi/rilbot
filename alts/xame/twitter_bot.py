# Run: py twitter_bot.py
from auth import api
from datetime import datetime
from twitter_winner import winner

# Create class instance
win = winner()

day = datetime.today().day

# Run script
if day in [3, 10, 17, 22, 26]:
  print("Xamexavu is meditating today.")
  pass
else:
  win.favorite_follow_retweet()

print(win.sort_file('twitterFilter.txt') + '\n')
