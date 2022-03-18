import tweepy
import fortune
import os
from auth import api_xame, api_uva, api_mevu, api_ril, api_zark


bots = [api_xame, api_uva, api_mevu, api_ril, api_zark]
coun = 0

def fort(api):
	fortune = os.popen("fortune fortunes").read()
	while len(fortune) > 280:
		fortune = os.popen("fortune fortunes").read()
		api.update_status(fortune)
		coun+=1
		print("{coun} fortuna postada")
		
for bot in bots:
	fort(bot)
