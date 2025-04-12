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

client = get_client()

def create_tweet(client, tweet): # funkcja do tweetowania
    client.create_tweet(text=tweet)

def wez_id(username): # funkcja do brania id uzytkownika
    try:
        user = client.get_user(username=username)
        print(user.data['id'])
    except tweepy.TooManyRequests as e:
        # to jak jest 429
        reset_time = int(e.response.headers['x-rate-limit-reset'])
        sleep_time = reset_time - time.time()

        print(f"Limit zapytan przekroczony. Czekam {sleep_time} sekund.")
        time.sleep(sleep_time + 1)  # Czekaj aż limit zostanie zresetowany
        wez_id(username)  # Ponów próbę




wybor = int(input("1 - wyślij tweet, 2 - wyszukaj info o uzytkowniku, 3 - wyslij dm (na razie nie działa)"))

# (prymitywna) obsluga funkcji

if wybor == 1:
    wiado = input("tresc twojego posta: ")
    print("twoja wiadomosc: " + wiado)
    client = get_client()
    create_tweet(client, wiado)

elif wybor == 2:
    uzytkownik = input("kogo wyszponcić?: ")
    wez_id(uzytkownik)
    print("user id " + uzytkownik)
    
elif wybor == 3:
    # user_id = input("id uzytkownika")
    # message = input("co chcesz wyslac do szponciciela?")
    # wyslij_dm(user_id, message)
    # print("wyslano chyba")
    print("nie działa, zrobie pozniej")
else:
    print("zle wpisales")





# try: 15717973539667312713
#     while True:
#         # czas = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#         # print(czas) 
#         wiado = input("tresc wiadomosci: ")
#         client = get_client()
#         create_tweet(client, wiado)

#         time.sleep(300) # 5 minut
# except KeyboardInterrupt:
#     print("elozelo")

