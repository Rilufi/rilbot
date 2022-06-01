import tweepy
import fortune
import os
from auth import api_xame, api_uva, api_mevu, api, api_zark, api_lufi


bots = [api_xame, api_uva, api_mevu, api, api_zark, api_lufi]
coun = 0


def get_chunks(s, maxlength):
    start = 0
    end = 0
    while start + maxlength  < len(s) and end != -1:
        end = s.rfind(" ", start, start + maxlength + 1)
        yield s[start:end]
        start = end +1
    yield s[start:]

def une(api):
	fortune = os.popen("fortune fortunes").read()
	if len(fortune) < 280:
		api.update_status(fortune)
	elif len(fortune) > 280:
		chunks = get_chunks(fortune, 280)

		chunkex = [(n) for n in chunks]

		coun = 0

		while coun < len(chunkex):
    			tweets = api.user_timeline(screen_name = api.me().screen_name, include_rts = False, count=1)
    			for tweet in tweets:
        			api.update_status(str(chunkex[coun]), in_reply_to_status_id = tweet.id, auto_populate_reply_metadata = True)
        			coun += 1
	else:
		pass
		
for bot in bots:
	une(bot)
	coun+=1
	print(f"{coun} fortuna postada")
