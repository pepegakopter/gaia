import tweepy
from dotenv import load_dotenv
import os
import time

def get_client():
    load_dotenv()

    client = tweepy.Client(
        consumer_key = os.getenv("CONSUMER_KEY"),
        consumer_secret = os.getenv("CONSUMER_SECRET"),
        access_token = os.getenv("ACCESS_TOKEN"),
        access_token_secret = os.getenv("ACCES_TOKEN_SECRET"),
        bearer_token= os.getenv("BEARER_TOKEN")
    )
    
    
    return client


def create_tweet(client, tweet):
    client.create_tweet(text=tweet)


try:
    while True:
        czas = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(czas) 

        client = get_client()
        create_tweet(client, "siema, o tej godzine wlecial tweet: " + czas)

        time.sleep(300) # 5 minut
except KeyboardInterrupt:
    print("elozelo")

