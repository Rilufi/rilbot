# Run: py twitter_bot.py
from auth import api
from datetime import datetime
#from twitter_winner import winner
from zark import quoter

# Create class instance
#win = winner()
quoter = quoter()
day = datetime.today().day

# Run script
if day in [4, 9, 14, 19, 24, 29]:
  print("Zark is nowhere to be found.")
  quoter.tweet_quote()
else:
  pass
 # win.favorite_follow_retweet()

#print(win.sort_file('twitterFilter.txt') + '\n')
