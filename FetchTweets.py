from dotenv import load_dotenv
import pandas as pd
import tweepy as tp
import os

load_dotenv(verbose=True)

auth = tp.AppAuthHandler(os.getenv("ACCESS_KEY"), os.getenv("SECRET_KEY"))

tweets = []

api = tp.API(auth)
for tweet in tp.Cursor(
    api.search,
    q="ifood",
    lang="pt",
    tweet_mode="extended",
).items(500):
    tweets.append(tweet.full_text.replace("\n", " "))

df = pd.DataFrame(columns=["Tweet"], data=tweets)

df.to_excel("iFood_Tweets.xlsx", encoding="UTF-8")