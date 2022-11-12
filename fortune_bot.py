import tweepy
import fortune
import os
from auth import api_xame, api_uva, api_mevu, api, api_zark, api_lufi, api_woba, api_maj, api_zeld, api_uff


bots = [api_xame, api_uva, api_mevu, api, api_zark, api_lufi, api_woba, api_maj, api_zeld, api_uff]

def une(api):
	fortune = os.popen("fortune alts/fortunes").read()
#	while len(fortune) < 280:
	if len(fortune) < 280:
		api.update_status(fortune)
	else:
		pass
		
for bot in bots:
	une(bot)
