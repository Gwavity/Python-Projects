import discord
import os
import random
from discord.ext import tasks

client = discord.Client()
pfpDirectory = r"Place your profile picture directory here" + "\\"

@client.event
async def on_ready():
    print("I'm ready")
    guild = client.get_guild()#Guild ID
    pfpChannel = guild.get_channel()#Channel ID for profile pictures
    bumpChannel = guild.get_channel()#Channel ID for bumping. If this is not a self bot then dyno will not accept the message.
    sendMessage.start(bumpChannel)
    sendPFP.start(pfpChannel)

@tasks.loop(hours=1)
async def sendPFP(channel):
    print("Sending pfp")
    pfps = os.listdir(pfpDirectory)
    imageDir = pfpDirectory + random.choice(pfps)
    imageFile = discord.File(imageDir)
    await channel.send(file=imageFile)
    os.remove(imageDir)

@tasks.loop(minutes=30)
async def sendMessage(channel):
    print("Bumping server")
    await channel.send("!d bump")

client.run("",bot=False)#"bot = False" allows for a self bot. If you are going use the bump feature then keep this how it is and just place your token in the quotes.
