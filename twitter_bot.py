# Run: py twitter_bot.py
from auth import api
from datetime import datetime
from twitter_winner import winner

# Create class instance
win = winner()
day = datetime.today().day

# Run script
if day in [1, 6, 11, 16, 26]:
  print("Rilufix is auditioning to be cast in Asterix and Obelix next movie.")
else:
  win.favorite_follow_retweet()

print(win.sort_file('twitterFilter.txt') + '\n')
