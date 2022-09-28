import tweepy
from auth import api


class rtquery:
    def rtquery(self):
        for tweet in tweepy.Cursor(api.search, q=f"#StarWars -filter:retweets -filter:replies filter:images", result_type="popular").items(2):
            try:
                api.create_favorite(tweet.id)
                tweet.retweet()
            except:
                pass
