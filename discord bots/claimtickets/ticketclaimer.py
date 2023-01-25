import requests
import time
import retrieveJSON

class autoClaim:
    def __init__(self,token,bot,guild,delay) -> None:
        self.token = token
        self.bot = bot
        self.guild = guild
        self.delay = delay
        self.channels = []
        self.headers = {'Authorization': token}
        self.newChannel = None

    def postClaim(self,message):
        print("\nPosting Claim")
        self.newChannel = None
        self.channels = []
        payload = {
            "type":3,
            "guild_id": self.guild,
            "channel_id": message["channel_id"],
            "application_id": message["author"]["id"],
            "message_id": message["id"],
            "session_id": "jkhasdlkasjd",
            "data": {"component_type":2,"custom_id": message['components'][0]['components'][0]['custom_id']}
        }
        time.sleep(self.delay)
        requests.post("https://discord.com/api/v10/interactions",json=payload,headers=self.headers)

    def getMessages(self):
        print("Getting Messages")
        
        while True:
            messages = requests.get(f"https://discordapp.com/api/v6/channels/{self.newChannel}/messages",headers=self.headers).json()
            if messages[0]["author"]["username"] == self.bot and len(messages[0]["components"]) >= 1:
                self.postClaim(messages[0])
                return
            
            print("Waiting 3 Seconds.")
            time.sleep(3)

    def retrieveChannels(self):
        while not self.newChannel:
            tempList = requests.get(f"https://discordapp.com/api/v6/guilds/{self.guild}/channels",headers=self.headers).json()
            
            if len(self.channels) == 0:
                currentRequest = requests.get(f"https://discordapp.com/api/v6/guilds/{self.guild}/channels",headers=self.headers).json()
                print("Setting channels")
                try:
                    for i in currentRequest:
                        self.channels.append(i["id"])
                except:
                    print("You are being rate limited!(Waiting 5 seconds)")
                    time.sleep(5)
            else:
                for i in range(100):
                    try:
                        tempName = tempList[i]["name"]
                        temp = tempList[i]["id"]
                        
                        if temp not in self.channels:
                            print(f"\n{temp}")
                            print(f"{tempName}\n")
                            self.newChannel = temp
                            self.getMessages()
                            break
                    except:
                        break
            print("Waiting 3 Seconds.")
            time.sleep(3)

if __name__ == "__main__":
    token,botName,guild,delay = retrieveJSON.getjson()
    claimer = autoClaim(token,botName,guild,delay)
    claimer.retrieveChannels()
