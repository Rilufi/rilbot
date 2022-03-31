# Run: py twitter_bot.py
from auth import api
from datetime import datetime
from twitter_clean_timeline import cleanTimeline
from twitter_unfollow import unfollow
from twitter_winner import winner

# Create class instance
win = winner()
unfollow = unfollow()
clean_timeline = cleanTimeline()

day = datetime.today().day

# Run script
if day == 3 or api.me().friends_count > 3000:
    try:
        unfollow.unfollow()
    except:
        pass
elif day in [5, 12, 19, 26] or api.me().favourites_count > 6000 or api.me().statuses_count > 6000:
    clean_timeline.unfavorite_unretweet()
else:
    win.favorite_follow_retweet()
print(win.sort_file('twitterFilter.txt') + '\n')
