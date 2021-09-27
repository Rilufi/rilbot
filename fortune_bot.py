from auth import *

api = tweepy.API(auth, wait_on_rate_limit = True)
COMMAND = "fortune"
fortune = os.popen(COMMAND).read()

while len(fortune) > 280:
	fortune = os.popen(COMMAND).read()

api.update_status(fortune)
