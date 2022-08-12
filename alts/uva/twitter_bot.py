# Run: py twitter_bot.py
from auth import api
from datetime import datetime
from twitter_winner import winner
from twitter_unfollow import unfollow
from uva import MarkovBot

# Create class instance
win = winner()
unfollow = unfollow()
tweetbot = MarkovBot()

day = datetime.today().day

# Run script
if day in [1, 7, 14, 21, 28]:
  print("Uva is on vacation.")
#  unfollow.unfollow()
  tweetbot.read('Freud_Dream_Psychology.txt')
  my_first_text = tweetbot.generate_text(25, seedword=[u'dream', u'psychoanalysis'])
  api.update_status('"'+my_first_text+'"')
else:
  win.favorite_follow_retweet()

print(win.sort_file('twitterFilter.txt') + '\n')
