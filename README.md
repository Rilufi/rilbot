# xamebot
Let's try to win some things on twitter with python

## tl;dr
Update auth.py with your credentials and run twitter_bot.py

## I beg your pardon?
so, I've read this https://qz.com/476914/i-built-a-twitter-bot-that-entered-and-won-1000-online-contests-for-me/ about some guy whom made a twitter bot to follow, favorite and RT tweets that contain contests and decided to make something like that (or at least try).

## Ok... but how
So after trying to adapt my idle bot for 5 minutes I've found blessed person that already did all the dirty work: https://github.com/robbiebarrat/twitter-contest-enterer and https://github.com/disestevez/Twitter-Giveaways-Bot indiscriminately copying their script. I've tried to run some sort of all-time here on github workflows (trying not to be banned and letting the API decide the limit plus some restrictions of usernames and words), but it didn't work because of the rate limit on tweepy, so I've scheduled the script to run every hour, then there's time for the limit to refresh, the first one didn't worked very well after the first try, so now I'm running the second version that only stops when reaches the workflow limit of 6 hours, so the next test will be to run every 7 hours (not 6 because of the time it takes to start each schedule). Every 6 hours is too much because there's the 400 limit to follow daily and it follows about 360 accounts in 6 hours, maybe the best way is to run only one time per day, let's see. I also adapted the code to run for 5h58min only for the scheduled task to be completed, ending before the 6 hours. It didn't work, twitter returned error code 226 (that's when he thinks we are a bot), so let's try once again, third time is the charm: I've found this other bot (twitter_bot.py) with a lot of gadgets like unfollow and clean timeline, it also just follow accounts that has a certain number of followers and with some description (trying to avoid fake accounts), last but not least: a filter, in which I've put things like tag (because it can't tag friends... it would be a nice feature tho) and like pinned tweets, 'cause the bot can't find them. This one will run only one time per day, to avoid twitter suspicion and following limits.

## So you will win MONEY???
Definetely not (actually not that definitely, as some prizes can be converted to money).

## So you will win... something?
Maybe, but probably will be something that I can't get (because there's little chance to send to Brazil and I'm trying to win contests written in a lot of languages, from everywhere) and in most cases it will be something useless, so I'll just contact the organizers and tell them to give the prize for someone else. But, in at least 1% of the cases I can actually win something.

## Then... why??
Well, like the rest of the bots, just to see if I can =)

## And now there is... fortunes?
Yep, I've put some fortunes to be posted everyday to end the monotony of the contests.

## Alright, where is it?
You can check the results on this account: [Rilufi](https://twitter.com/rilufix)
