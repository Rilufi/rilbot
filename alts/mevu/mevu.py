from auth import api
import random

class fact:
  def fact(self):
    lines=open('alts/Facts.txt').read().splitlines()
    print(lines)
    status = random.choice(lines)
    api.create_tweet(text = status)
