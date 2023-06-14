from auth import api
import random

class fact:
  def fact(self):
    lines=open('alts/Facts.txt').read().splitlines()
    status = random.choice(lines)
    print(status)
    api.create_tweet(text = status)
