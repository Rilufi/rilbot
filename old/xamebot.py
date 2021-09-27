#! /usr/bin/env python
# coding=utf-8

import tweepy
import os

#calling secret variables
CONSUMER_KEY = os.environ["CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]


#connect on twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
keywords = ["rt to", "rt and win", "retweet and win", "rt for", "rt 4", "retweet to"]

bannedwords = ["vote", "bot", "b0t"]

bannedusers = ['bot', 'spot', 'lvbroadcasting', 'jflessauSpam', 'bryster125', 'MobileTekReview', 'ilove70315673', 'followandrt2win', 'traunte', 'ericsonabby', '_aekkaphon'] # does not need to be the entire username! you can just put 'bot' for names like 'b0tspotter', etc.

def is_user_bot_hunter(username):
	clean_username = username.replace("0", "o")
	clean_username = clean_username.lower()
	for i in bannedusers:
		if i in clean_username:
			return True
		else:
			return False

def search(twts):
	for i in twts:
		if not any(k in i.text.lower() for k in keywords) or any(k in i.text.lower() for k in bannedwords):
			continue
		if is_user_bot_hunter(str(i.author.screen_name)) == False:
			if not i.retweeted:
				try:
					api.retweet(i.id)
					print("rt " + (i.text))
					
					# huge thanks to github user andrewkerr5 for providing the fix for hashtags
					if "follow" in i.text or "#follow" in i.text or "Follow" in i.text or "#Follow" in i.text or "FOLLOW" in i.text or "#FOLLOW" in i.text or "following" in i.text or "#following" in i.text or "FOLLOWING" in i.text or "#FOLLOWING" or "Following" in i.text or "#Following" in i.text:
						user_id = i.retweeted_status.user.id
						api.create_friendship(user_id)

				except Exception:
					pass
				
			if ("fav" in i.text or "Fav" in i.text or "FAV" in i.text) and not i.favorited:
				try:
					api.create_favorite(i.id)
					print("fav " + (i.text))
				except Exception:
					pass
			



def run():
	for key in ["RT to win", "retweet to win"]:
		print("\nSearching again\n")
		search(api.search(q=key))


if __name__ == '__main__':
	while True:
		run()
