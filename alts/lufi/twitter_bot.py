# Run: py twitter_bot.py
from auth import api
from datetime import datetime
from twitter_winner import winner
from twitter_unfollow import unfollow
from lufi import quoter

# Create class instance
win = winner()
unfollow = unfollow()
quoter = quoter()

day = datetime.today().day

# Run script
if day in [6, 12, 18, 24, 29]:
  print("Lufilir don't work today.")
#  unfollow.unfollow()
  quoter.tweet_quote()
else:
  win.favorite_follow_retweet()

print(win.sort_file('twitterFilter.txt') + '\n')
