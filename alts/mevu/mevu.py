from auth import api
import random

class fact:
  def fact(self):
    lines=open('Facts.txt').read().splitlines()
    print(lines)
    status = random.choice(lines)
    api.update_status(status)
