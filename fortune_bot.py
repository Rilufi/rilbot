import tweepy
import fortune
import os
from auth import api_xame, api_uva, api_mevu, api, api_zark, api_lufi, api_woba, api_maj, api_zeld
#from twitter_unfollow import unfollow


bots = [api_xame, api_uva, api_mevu, api, api_zark, api_lufi, api_woba, api_maj, api_zeld, api_uff]

def une(api):
	fortune = os.popen("fortune alts/fortunes").read()
	my_screen_name = api.me().screen_name
#	while len(fortune) < 280:
	if len(fortune) < 280:
		api.update_status(fortune)
		print(f"fortuna p/ {my_screen_name} rolou")
	else:
		print(f"sem fortuna p/ {my_screen_name} hoje")
		pass
	
	
for bot in bots:
	une(bot)
#	try:
#		unfollow(bot)
#	except:
#		pass
