import json
import random
from auth import api

def get_quotes():
    with open('data.json') as f:
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
            """.format(quote['quote'], quote['movie'])
    return tweet

def tweet_quote():
    print('getting a random quote...')        
    tweet = create_tweet()
    api.update_status(tweet)
    print(tweet)   

if __name__ == "__main__":
    tweet_quote()
