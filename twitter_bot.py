# Run: py twitter_bot.py
from datetime import datetime
from twitter_winner import winner
from auth import api_xame, api_uva, api_mevu, api_ril, api_zark, api_lufi

# Create class instance
win = winner()
day = datetime.today().day

# Run script
if day in [4, 8, 13, 19, 25]:
  print("Rilufix is auditioning to be cast in Asterix and Obelix next movie.")
  pass
else:
  api = api_ril
  win.favorite_follow_retweet()

print(win.sort_file('twitterFilter.txt') + '\n')

if day in [5, 9, 15, 23, 30]:
  print("Mevuxa is not home today.")
  pass
else:
  api = api_mevu
  win.favorite_follow_retweet()

print(win.sort_file('twitterFilter.txt') + '\n')

if day in [6, 12, 18, 24, 29]:
  print("Lufilir don't work today.")
  pass
else:
  api = api_lufi
  win.favorite_follow_retweet()

print(win.sort_file('twitterFilter.txt') + '\n')

if day in [1, 7, 14, 21, 28]:
  print("Uvaxemax is on vacation.")
  pass
else:
  api = api_uva
  win.favorite_follow_retweet()

print(win.sort_file('twitterFilter.txt') + '\n')

if day in [2, 11, 16, 20, 27]:
  print("Zarknall is nowhere to be found.")
  pass
else:
  api = api_zark
  win.favorite_follow_retweet()

print(win.sort_file('twitterFilter.txt') + '\n')

if day in [3, 10, 17, 22, 26]:
  print("Xamexavu is meditating today.")
  pass
else:
  api = api_xame
  win.favorite_follow_retweet()

print(win.sort_file('twitterFilter.txt') + '\n')
