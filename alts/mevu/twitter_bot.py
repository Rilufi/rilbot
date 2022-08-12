# Run: py twitter_bot.py
from auth import api
from datetime import datetime
from twitter_winner import winner
from twitter_unfollow import unfollow
from mevu import fact

# Create class instance
win = winner()
unfollow = unfollow()
fact = fact()

day = datetime.today().day

# Run script
if day in [5, 9, 15, 23, 30]:
  print("Mevu is not home today.")
#  unfollow.unfollow()
  fact.fact()
else:
  win.favorite_follow_retweet()

print(win.sort_file('twitterFilter.txt') + '\n')
