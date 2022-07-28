from auth import api
import random

class fact:
  def fact(self):
    lines=open('Factx.txt').read().splitlines()
    print(lines)
    status = random.choice(lines)
    api.update_status(status)
