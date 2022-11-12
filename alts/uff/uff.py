import tweepy
from auth import api


class rtquery:
    def rtquery(self):
        for tweet in tweepy.Cursor(api.search, q=f"Cryptocurrency -filter:retweets -filter:replies filter:images", result_type="popular").items(3):
            try:
                api.create_favorite(tweet.id)
                tweet.retweet()
            except:
                pass
