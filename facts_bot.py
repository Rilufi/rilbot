import tweepy
from random import randint
from auth import api
import pandas

infile = open('Facts.txt', 'r')
Facts = []
for line in infile:
    Facts.append(line.strip('\n'))
infile.close()

Hashtags = ['#science', '#facts', '#interestingfact', '#hmmm', '#follow', '#interesting', '#factoid', '#funfact', '#wow', '#braindrop']

df = pandas.read_csv('Log.csv')
i = int(df.values[0][0])
new_i = i + 1
df.at[0,"Fatos"] = new_i
df.to_csv('Log.csv', index=False)

api.update_status(Facts[i]+' '+Hashtags[randint(0,len(Hashtags)-1)]) # Tweet a fact as well as a random hashtag
