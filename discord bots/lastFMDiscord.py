#Retrieved some of my functions from here: https://github.com/huberf/lastfm-scrobbler/blob/master/lastpy/__init__.py
#Just changed them up a little.
import requests
import time
import hashlib
import discord
import asyncio
from discord.ext import commands

APIKEY = ""#Pass your LastFM API Key in here.
SECRETKEY = ""#Pass your LastFM SECRET Key in here.

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all(), case_insensitive=True)
activeScrobblers = {}
#"userID":["sessionKey",False/True]

tokenURL = f"http://ws.audioscrobbler.com/2.0/?method=auth.gettoken&api_key={APIKEY}&format=json"

def sessionSig(token):
    params = {
        "api_key": APIKEY,
        "method": "auth.getSession",
        "token": token,
    }
    resquestHash = hashRequest(params,SECRETKEY)
    params["api_sig"] = resquestHash
    params["format"] = "json" 

    return params

def createScrobbleSig(track,artist,sk):
    params = {
        'method': 'track.scrobble',
        'api_key': APIKEY,
        'timestamp': time.time(),
        'track': track,
        'artist': artist,
        'sk': sk
    }
    requestHash = hashRequest(params,SECRETKEY)
    params["api_sig"] = requestHash

    return params
 
def hashRequest(obj, secretKey):
    string = ''
    items = obj.keys()
    for i in sorted(items):
        string += i
        string += str(obj[i])
        
    string += secretKey
    stringToHash = string.encode('utf8')
    requestHash = hashlib.md5(stringToHash).hexdigest()

    return requestHash

def createEmbed(instance,token=None,artist = None,track = None):
    if instance == "commandError":
        embed = discord.Embed(title="Please provide an artist and track in the order (**$fmScrobble artist name track name**)\nIn order to use songs/artists with spaces in their names, use quotes around the name.",color=discord.Color.from_rgb(255,0,0))
    if instance == "connect":
        embed = discord.Embed(title="Connect your last.fm account to the bot.",description=f"http://www.last.fm/api/auth/?api_key={APIKEY}&token={token}",color=discord.Color.from_rgb(255,0,0))
    if instance == "currentlyScrobbling":
        embed = discord.Embed(title="You are already scrobbling.",description="No need to run this command again.",color=discord.Color.from_rgb(255,0,0))
    if instance == "success":
        embed = discord.Embed(title=f"You are scrobbling: {artist} {track.capitalize()}.\n Type $fmstop to end your scrobbling.",color=discord.Color.green())
    if instance == "rateLimit":
        embed = discord.Embed(title="You are currently being rate-limited.",description="Please wait a little while before using this bot again.",color=discord.Color.from_rgb(255,0,0))
    if instance == "finishedScroblbing":
        embed = discord.Embed(title="You are finished scrobbling.",description=f"Scrobbled track: {artist}-{track}",color=discord.Color.green())
    if instance == "stoppingError":
        embed = discord.Embed(title="You aren't currently scrobbling a song.",description="No need to run this command again.",color=discord.Color.from_rgb(255,0,0))

    embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/B3Zu6zRtbXcj7XMbKhHjgp0_I762Z-3vEQrEFj1noJA/https/www.last.fm/static/images/lastfm_logo_facebook.15d8133be114.png?width=1278&height=671")
    return embed

@bot.event
async def on_ready():
    print(bot.user.name, "is ready.")

@bot.command()
async def fmScrobble(ctx,*args):
    increment = 0
    if len(args) <= 1 or len(args) > 2:
        await ctx.reply(embed=createEmbed("commandError"))
        return
    
    if ctx.author.id not in activeScrobblers:
        token = requests.get(tokenURL).json()["token"]
        await ctx.reply(embed=createEmbed("connect",token))
    else:
        if not activeScrobblers[ctx.author.id]: 
            await ctx.reply(embed=createEmbed("currentlyScrobbling"))
            return
    currentTime = time.time()

    while ctx.author.id not in activeScrobblers:
        if time.time() - currentTime >= 10:#Exits the function if the user doesn't create their token in time.
            await ctx.reply("Revoking session.")
            return
        try:
            params = sessionSig(token)
            response = requests.get("http://ws.audioscrobbler.com/2.0/",params)
            
            if response.status_code == 200:
                sessionKey = response.json()["session"]["key"]
                activeScrobblers[ctx.author.id] = [sessionKey]
        except:
            pass
    
    activeScrobblers[ctx.author.id][1] = True
    while ctx.author.id in activeScrobblers:
#         if increment >= 200:
#             break

        params = createScrobbleSig(args[1],args[0],activeScrobblers[ctx.author.id][0])
        response = requests.post("http://ws.audioscrobbler.com/2.0/",params).text
        if increment == 0:
            await ctx.reply(embed=createEmbed("success",artist=args[0],track=args[1]))
        if "Rate Limit Exceed" in response:
            await ctx.reply(embed=createEmbed("rateLimit"))
            return

        await asyncio.sleep(0.1)
        increment += 1
    
    await ctx.reply(embed=createEmbed("finishedScroblbing",None,args[0],args[1]))
    activeScrobblers[ctx.author.id][1] = False

@bot.command()
async def fmStop(ctx):
   if ctx.author.id in activeScrobblers and activeScrobblers[ctx.author.id][1]:
        activeScrobblers[ctx.author.id][1] = False
    else:
        await ctx.reply(embed=createEmbed("stoppingError"))

bot.run("")#Place your discord bot Token in here.
