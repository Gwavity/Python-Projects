import requests
import datetime
import discord
from discord.ext import commands

intent = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intent, case_insensitive=True)
developerKey = ""

@bot.event
async def on_ready():
    print(bot.user.name, "is ready.")

def getSteamID(steamID64):
    authserver = (int(steamID64) - 76561197960265728) & 1
    authid = (int(steamID64) - 76561197960265728 - authserver) / 2
    
    return f"STEAM_0:{authserver}:{int(authid)}"

def getSteamID64(url):
    requestURL = f"http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={developerKey}&vanityurl="
    if "profile" in url:
        urlID = url[url.find("profiles/") + 9:]
        steamID64 = urlID
    else:
        urlID = url[url.find("id/") + 3:]
        if urlID[-1] == "/":
            urlID = urlID[:-1]
        steamID64 = requests.get(requestURL + urlID).json()["response"]["steamid"]
        
    return steamID64

def getIDs(url):
    steamID64 = getSteamID64(url)
    steamID = getSteamID(steamID64)
    
    return steamID64,steamID

def userData(url):
    steamdIDs = getIDs(url)
    requestURL = f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={developerKey}&steamids={steamdIDs[0]}"
    response = requests.get(requestURL).json()["response"]
    player = response["players"][0]
    
    accountCreation = datetime.datetime.fromtimestamp(player["timecreated"])
    accountCreationDate = accountCreation.strftime("%m/%d/%Y")
    creationInfo = f"Creation date: {accountCreationDate} | Approximately {round((datetime.datetime.now() - accountCreation).days / 365,1)} years ago."
    
    username = player["personaname"]
    customURL = player["profileurl"]
    avatarURL = player["avatarfull"]
    
    return customURL,username,steamdIDs,avatarURL,creationInfo

@bot.command()
async def getID(ctx,url):
    info = userData(url)
    steamID64 = info[2][0]
    steamID = info[2][1]
    
    embed = discord.Embed(url=info[0],title=info[1],description=f"SteamID: {steamID}\nSteamID64: {steamID64}\nCustom Profile URL: {info[0]}\nFull Profile URL: https://steamcommunity.com/profiles/{steamID64}",color=discord.Color.random())
    embed.set_thumbnail(url=info[-2])
    embed.set_footer(text=info[-1])
    
    await ctx.reply(embed=embed)
    
bot.run("")# Discord bot token
