# Run: py twitter_bot.py
from auth import api
from datetime import datetime
#from twitter_winner import winner
#from maj import rtquery

# Create class instance
#win = winner()
#rt = rtquery()
day = datetime.today().day

# Run script
if day in [3, 8, 13, 18, 23, 28]:
  print("Majin is in a really rage right now.")
#  rt.rtquery()
else:
  pass
#  win.favorite_follow_retweet()

#print(win.sort_file('twitterFilter.txt') + '\n')
