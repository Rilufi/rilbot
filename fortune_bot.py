import tweepy
import fortune
import os
from auth import api_xame, api_uva, api_mevu, api, api_zark, api_lufi, api_maj, api_zeld
#from twitter_unfollow import unfollow


bots = [api_xame, api_uva, api_mevu, api, api_zark, api_lufi, api_maj, api_zeld]

count = 0

def une(api):
	fortune = os.popen("fortune alts/fortunes").read()
	count += 1
#	my_screen_name = api.me().screen_name
#	while len(fortune) < 280:
	if len(fortune) < 280:
		api.create_tweet(text = fortune)
		print(f"fortuna {count} rolou")
	else:
		print(f"fortuna {count} não rolou")
		pass
	
	
for bot in bots:
	une(bot)
#	try:
#		unfollow(bot)
#	except:
#		pass
