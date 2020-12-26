import requests
import random

auth = "Bearer cUR_17Bs17xRvRzStIv4"
#Books

response = requests.get("https://the-one-api.dev/v2/book", headers = {"Authorization": auth})
docs = response.json()["docs"]
books = [print(x['name']) for x in docs]


#Movies
#response = requests.get("https://the-one-api.dev/v2/movie", headers = {"Authorization": auth})
#print(response.json())
#docs = response.json()["docs"]
#movie = [print(x['name']) for x in docs]

#Characters

#while True:
   # randomId = random.randint(0, 940)
    #response = requests.get("https://the-one-api.dev/v2/character", headers = {"Authorization": auth})
 #   docs = response.json()["docs"]
  #  print("Name: " + docs[randomId]["name"])
   # print("Birth: " + docs[randomId]["birth"])
#    print("Death: " + docs[randomId]["death"])
 #   print("Race: " + docs[randomId]["race"])
  #  print("Gender: " + docs[randomId]["gender"])
   # print("From the realm of: " + docs[randomId]["realm"])
   # print("Spouse: " + docs[randomId]["spouse"])
    #print("Not everything is known about these characters, if the value is blank or NaN it means that it simply isn't known, isn't relevant or isn't the database yet.")
    #print("====================================")
    #breakVar = input("new character? (Y/N) ")
    #if breakVar == "y" or breakVar == "Y":
     #   continue
    #elif breakVar == "n" or breakVar == "N":
      #  break


#randomId = random.randint(0, 999)
#response = requests.get("https://the-one-api.dev/v2/quote", headers = {"Authorization": auth})
#docs = response.json()["docs"]

#print("Quote: '" + docs[randomId]["dialog"]+"'")
