import requests
import json
import random

#AccessToken Webex, enkel 12u geldig
accessToken = "Bearer NDVkNTM0NjQtZmYwMy00MTU4LTllNTMtZjZiYWQ4ODQ1ZWU0OGU4OGY0ZTItZWM1_PF84_consumer"

#Auth key voor LOTR API
auth = "Bearer cUR_17Bs17xRvRzStIv4"

#Rooms API gebruiken
resp = requests.get(   "https://api.ciscospark.com/v1/rooms",
                    headers = {"Authorization": accessToken}
                )
#Rooms printen
print("Lijst van alle rooms:")
rooms = resp.json()["items"]
for room in rooms:
    print (room["title"])
    
while True:
    # Input om aan te geven waar hij achter bot commands moet zoeken 
    zoekDit = input("Waar wil je dat de bot luistert? Geef de exacte naam in: ")

    #roomId variabele setten
    roomId = None
    
    for room in rooms:
        # Zoekt "title" door gebruik te maken van mijn input bij de variabele zoekDit 
        if(room["title"].find(zoekDit) != -1):
            print ("Gevonden rooms met uw zoekopdracht " + room["title"])

            # Titel en id worden opgeslagen in variables
            roomId = room["id"]
            roomTitle = room["title"]
            print("Found room : " + roomTitle)
            break

    if(roomId == None):
        print("Niks gevonden met " + zoekDit )
        print("Probeer opnieuw...")
    else:
        break

#Bot loop
while True:

    #parameters die ik mee geef bij het HTTP GET request
    getParameters = {
        "roomId": roomId,
        "max": 1
        #max:1 is om enkel het laatste bericht te gebruiken wanneer hij een message zoekt
        }
    
    r = requests.get("https://api.ciscospark.com/v1/messages", 
                         params = getParameters, 
                         headers = {"Authorization": accessToken}
                    )

    jsonData = r.json()
    # kijken als er berichten in de room zitten, zo niet, exception
    if len(jsonData["items"]) == 0:
        raise Exception("Geen berichten in de room")
    
    # alle berichten "opslaan"
    messages = jsonData["items"]
    # tekst van het meest recente bericht opslaan in een andere variabele, met deze werken we.
    message = messages[0]["text"]


    
    print("Ik zag dit bericht: " + message)

    #help-menu voor bot
    if message == "/help":
        print("De volgende commando's kunt u uitvoeren: \n",
              "help: Pretty obvious, isn't it?\n",
              "movies: Geef alle Lord Of The Rings films via The One API\n",
              "books: Geef alle Lord Of The Rings boeken via The One API\n",
              "character: Geef een willekeurig karakter die in Tolkiens universum bestaat\n",
              "quote: Geef een willekeurge quote van een karakter die in Tolkiens universum bestaat\n")

    #Alle films printen
    if message == "/movies":
        response = requests.get("https://the-one-api.dev/v2/movie", headers = {"Authorization": auth})
        print(response.json())
        docs = response.json()["docs"]
        movie = [print(x['name']) for x in docs]

    #Alle boeken printen
    if message == "/books":
        response = requests.get("https://the-one-api.dev/v2/book", headers = {"Authorization": auth})
        docs = response.json()["docs"]
        books = [print(x['name']) for x in docs]

    #print random character
    if message == "/character":
        while True:
            randomId = random.randint(0, 940)
            response = requests.get("https://the-one-api.dev/v2/character", headers = {"Authorization": auth})
            docs = response.json()["docs"]
            print("Name: " + docs[randomId]["name"])
            print("Birth: " + docs[randomId]["birth"])
            print("Death: " + docs[randomId]["death"])
            print("Race: " + docs[randomId]["race"])
            print("Gender: " + docs[randomId]["gender"])
            print("From the realm of: " + docs[randomId]["realm"])
            print("Spouse: " + docs[randomId]["spouse"])
            print("Not everything is known about these characters, if the value is blank or NaN it means that it simply isn't known, isn't relevant or isn't the database yet.")
            print("====================================")
            breakVar = input("new character? (Y/N) ")
            if breakVar == "y" or breakVar == "Y":
                continue
            elif breakVar == "n" or breakVar == "N":
                break

            
    #print random quotes
    if message == "/quote":
        randomId = random.randint(0, 999)
        response = requests.get("https://the-one-api.dev/v2/quote", headers = {"Authorization": auth})
        docs = response.json()["docs"]
        print("Quote: '" + docs[randomId]["dialog"]+"'")


