import json
import pyotp
import pyclip 

with open("authSecrets.json","r") as readSecret:
    auth = json.load(readSecret)

while True:
    for i, sec in enumerate(auth):
        print(i + 1, sec,"- " + auth[sec]["name"])
    
    choice = int(input("\nWhich app would you like your AUTH code for? ")) - 1

    authDetails = auth[list(auth.keys())[choice]]
    key = pyotp.TOTP(authDetails["secret"]).now()
    pyclip.copy(key)
  
    print(f"Copied authentication key to clipboard: {key}\n")
