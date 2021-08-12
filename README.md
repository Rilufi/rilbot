# xamebot
Let's try to win some things on twitter with python

## I beg your pardon?
so, I've read this https://qz.com/476914/i-built-a-twitter-bot-that-entered-and-won-1000-online-contests-for-me/ about some guy whom made a twitter bot to follow, favorite and RT tweets that contain contests and decided to make something like that (or at least try).

## Ok... but how
So after trying to adapt my idle bot for 5 minutes I've found blessed person that already did all the dirty work: https://github.com/robbiebarrat/twitter-contest-enterer and https://github.com/disestevez/Twitter-Giveaways-Bot indiscriminately copying their script. I've tried to run some sort of all-time here on github workflows (trying not to be banned and letting the API decide the limit plus some restrictions of usernames and words), but it didn't work because of the rate limit on tweepy, so I've scheduled the script to run every hour, then there's time for the limit to refresh, the first one didn't worked very well after the first try, so now I'm running the second version that only stops when reaches the workflow limit of 6 hours, so the next test will be to run every 7 hours (not 6 because of the time it takes to start each schedule)

## So you will win MONEY???
Definetely not.

## So you will win... something?
Maybe, but probably that will be something that I can't get (because Brazil and I'm trying to win contests written in english) and in most cases it will be something useless, so I'll just contact the organizers and tell them to give the prize for someone else. But, in at least 1% of the cases I can actually win something.

## Then... why??
Well, like the rest of the bots, just to see if I can =)

## Alright, where is it?
You can check the results on this account: https://twitter.com/xamexavu
