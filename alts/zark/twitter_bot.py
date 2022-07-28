# Run: py twitter_bot.py
from auth import api
from datetime import datetime
from twitter_winner import winner
from twitter_unfollow import unfollow
from zark import quoter

# Create class instance
win = winner()
unfollow = unfollow()
quoter = quoter()

day = datetime.today().day

# Run script
if day in [2, 11, 16, 20, 27]:
  print("Zark is nowhere to be found.")
  quoter.tweet_quote()
  unfollow.unfollow()
else:
  win.favorite_follow_retweet()

print(win.sort_file('twitterFilter.txt') + '\n')
