import requests
import json
import time

#AccessToken, enkel 12u geldig
accessToken = "Bearer YTFhNjVlODYtNzU5My00MzQ0LWEwNDEtODgxMTA4MjYyYTJmZDZmNDk2ZjctZjVh_PF84_consumer"

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

    #roomId variabele
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
    #1 seconde delay, ik wil niet over het limiet van API calls gaan
    time.sleep(1)

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
    # kijken als er berichten in de room zitten
    if len(jsonData["items"]) == 0:
        raise Exception("Geen berichten in de room")
    
    # alle berichten opslaan
    messages = jsonData["items"]
    # tekst van het eerste bericht opslaan in een andere variabele
    message = messages[0]["text"]
    print("Ik zag dit bericht: " + message)
    
