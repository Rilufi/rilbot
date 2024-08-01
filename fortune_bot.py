import tweepy
import fortune
import os
from auth import api_xame, api_uva, api_mevu, api_zark, api_lufi, api_maj, api_zeld
#from twitter_unfollow import unfollow

bots = [api_xame, api_uva, api_mevu, api_zark, api_lufi, api_maj, api_zeld]

count = 0

def une(api, bot_name):
    fortune_text = os.popen("fortune alts/fortunes").read()
    global count
    count += 1
    try:
        if len(fortune_text) < 280:
            api.create_tweet(text=fortune_text)
            print(f"fortuna {count} rolou para {bot_name}")
        else:
            print(f"fortuna {count} não rolou para {bot_name}")
    except tweepy.errors.Unauthorized as e:
        print(f"Erro de autenticação para {bot_name}: {e}")
    except Exception as e:
        print(f"Erro ao postar para {bot_name}: {e}")

for bot, bot_name in zip(bots, ['api_xame', 'api_uva', 'api_mevu', 'api_zark', 'api_lufi', 'api_maj', 'api_zeld']):
    une(bot, bot_name)
