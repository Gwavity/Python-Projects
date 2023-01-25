import json

def getjson():
    with open("parameters.json","r") as info:
        info = json.load(info)
        token = info["token"]
        botName = info["botname"]
        guild = info["guild"]
        delay = info["delay"]
    return token,botName,guild,delay