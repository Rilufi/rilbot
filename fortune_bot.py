from auth import api
import fortune
import os

fortune = os.popen("fortune fortunes").read()
while len(fortune) > 280:
	fortune = os.popen("fortune fortunes").read()
api.update_status(fortune)

