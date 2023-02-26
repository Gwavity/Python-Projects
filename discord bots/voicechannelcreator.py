import discord
from discord.ext import commands 
import random
from time import time

intent = discord.Intents.all()
bot = commands.Bot(command_prefix="$",intents=intent)

wordList = [] #Fill this list with words for each channel.

guild = None #Stores guild
vcCategory = None #Stores category with VCs

@bot.event
async def on_ready():
    print("Im ready!")

@bot.before_invoke
async def getCategory(ctx):
    global guild
    global vcCategory
    guild = ctx.guild #Retrieves the guild
    categories = guild.categories #Gets all categories in the guild
    for category in categories:
        if len(category.voice_channels) >= 2: #If the category has more than 2 voice channels then it continues
            vcCategory = category #Saves the category with the VCs
            break #Breaks the loop when it finds the first category with VCs.

@bot.command()
async def c(ctx,name,count = 1):
    startTime = time()
    for i in range(int(count)):# Loops the amount of times the user enters.
        try:
            await guild.create_voice_channel(name + str(i + 1),category=vcCategory)# Creates as many channels as the user wants with inputted name.
        except:
            await ctx.send("Too many channels in: \"" + vcCategory.name + "\". MAX IS 50!")
            break
    await ctx.send(f"Done creating {count} channels.\n`Completion took {round(time() - startTime,2)}s`")

@bot.command()
async def cRandom(ctx,count):
    ## Allows you to add overwrites to a channel
    ## Syntax: example- {'role': discord.PermissionOverwrite(connect=False,speak=True)}
    ## False denies. True allows. Not including permission does nothing
    # overwrite = {
    #     guild.default_role: discord.PermissionOverwrite(view_channel=False)
    # }
    startTime = time()
    for i in range(int(count)): #Loops the amount of times the user enters.
        caps = random.randint(0,1) #Picks if the word will be a capital
        word = random.choice(wordList) #Chooses a random word
        if caps:
            word = word.capitalize()
        else:
            word = word.lower()
        try:
            await guild.create_voice_channel(word,category=vcCategory) #Add 'overwrites=overwrite' at the end for specific permissions #Creates as many channels as the user wants with a random name.
        except:
            await ctx.send("Too many channels in: \"" + vcCategory.name + "\". MAX IS 50")
            break
    await ctx.send(f"Done creating {count} channels.\n`Completion took {round(time() - startTime,2)}s`")

bot.run("")
