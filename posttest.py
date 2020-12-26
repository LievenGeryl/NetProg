import requests
import json
import random

#AccessToken Webex, enkel 12u geldig
accessToken = "Bearer NDNjNmRiNmUtZTlkMi00OTZiLWEwYTktZmMxOWYxNjY5ZTEwM2M3ZGJiN2ItMjI5_PF84_consumer"
roomId = "Y2lzY29zcGFyazovL3VzL1JPT00vMjQ0YmY0ODAtMDE2ZS0xMWViLTg5NmMtODMwMDFlY2VhNDk3"




PostData = {
    "roomId": roomId,
    "text": "AARDAPPEL"
    }

r = requests.post( "https://webexapis.com/v1/messages", 
    headers = HTTPHeaders, 
    data = json.dumps(PostData)
    )

print(r)
