# Run: py twitter_bot.py
from auth import api
from datetime import datetime
#from twitter_winner import winner
from lufi import quoter

# Create class instance
#win = winner()
quoter = quoter()
day = datetime.today().day

# Run script
if day in [2, 7, 12, 17, 22, 27]:
  print("Lufilir don't work today.")
  quoter.tweet_quote()
else:
  pass
#  win.favorite_follow_retweet()

#print(win.sort_file('twitterFilter.txt') + '\n')
