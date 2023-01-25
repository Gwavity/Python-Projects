import json
from pathlib import Path

def getjson():
    with open(f"{Path(__file__).parent}\parameters.json","r") as info:
        info = json.load(info)
        token = info["token"]
        botName = info["botname"]
        guild = info["guild"]
        delay = info["delay"]
    return token,botName,guild,delay
