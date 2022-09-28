import tweepy
from auth import api


class rtquery:
    def rtquery(self):
        for tweet in tweepy.Cursor(api.search, q=f"Tetris -filter:retweets -filter:replies filter:images", result_type="recent").items(1):
            try:
                api.create_favorite(tweet.id)
                tweet.retweet()
            except:
                pass
