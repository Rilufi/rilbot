# Run: py twitter_bot.py
from auth import api
from datetime import datetime
#from twitter_winner import winner
#from zeld import rtquery

# Create class instance
#win = winner()
#rt = rtquery()
day = datetime.today().day

# Run script
if day in [5, 10, 15, 20, 25, 30]:
  print("Zelda doesn't even care about Link.")
#  rt.rtquery()
else:
#  win.favorite_follow_retweet()

#print(win.sort_file('twitterFilter.txt') + '\n')
