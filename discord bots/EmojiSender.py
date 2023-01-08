#https://discord.com/developers/docs/resources/emoji#list-guild-emojis
#https://github.com/owersite/invisible-tag/blob/master/invisible%20tag%20exploit.py Learned about sending messages from this
import requests
import random
import time

randomTimes = [60,70,80,90,100,120]
channelIDs = [] 

class SendMessage:
    def __init__(self, token, channel, guild_id):
        self.token = token
        self.channelIDs = channel
        self.guild_id = guild_id
        self.headers = {'Authorization': token}

    def getEmoji(self):
        emojiUrl = f"https://discordapp.com/api/v6/guilds/{self.guild_id}/emojis"
        emoji = random.choice(requests.get(emojiUrl,headers=self.headers).json())
        return emoji["name"],emoji["id"]

    def run(self):
        while True:
            emojiMessage = "<:{0}:{1}>".format(*self.getEmoji())
            if isinstance(self.channelIDs,list):
                sendingChannel = random.choice(self.channelIDs)
            else:
                sendingChannel = self.channelIDs

            channelName = requests.get(f"https://discordapp.com/api/v6/channels/{sendingChannel}",headers=self.headers).json()["name"]
            print(f"Sending emoji in {channelName}!!")
            requests.post(f'https://discordapp.com/api/v6/channels/{sendingChannel}/messages', headers=self.headers,json={"content":emojiMessage})
            
            sleepTime = random.choice(randomTimes)
            print(f"Sleeping for {sleepTime}s!!")
            time.sleep(random.choice(randomTimes))

def main():
    token = input("Enter Token: ")
    channelIDs = input("Enter channelID(seperate with commas for multiple channels): ")
    if "," in channelIDs:
        channelIDs = channelIDs.split(',')
    guild_id = int(input("Ener GuildID: "))
    
    messageClass = SendMessage(token, channelIDs, guild_id)
    messageClass.run()

if __name__ == '__main__':
    main()
