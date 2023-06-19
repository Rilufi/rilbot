import json
import random
from auth import api

def get_quotes():
    with open('alts/got.json') as f:
        quotes_json = json.load(f)
    return quotes_json['quotes']

def get_random_quote():
    quotes = get_quotes()
    random_quote = random.choice(quotes)
    return random_quote

def create_tweet():
    quote = get_random_quote()
    tweet = """
            "{}"
            -{}
            """.format(quote['quote'], quote['character'])
    return tweet

class quoter:
    def tweet_quote(self):
        print('getting a random quote...')        
        tweet = create_tweet()
        api.create_tweet(text = tweet)
        print(tweet)
