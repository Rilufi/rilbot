# Run: py twitter_bot.py
from auth import api
from datetime import datetime
from twitter_winner import winner
from mevu import fact

# Create class instance
win = winner()
fact = fact()
day = datetime.today().day

# Run script
if day in [4, 9, 14, 19, 24, 29]:
  print("Mevu is not home today.")
  fact.fact()
else:
  win.favorite_follow_retweet()

print(win.sort_file('twitterFilter.txt') + '\n')
