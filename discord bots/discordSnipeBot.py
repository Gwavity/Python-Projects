import discord
import random
from discord.ext import commands

intent = discord.Intents.all()
bot = commands.Bot(command_prefix="$",intents=intent)
deletedMessage = ""

@bot.event
async def on_ready():
    print("I'm ready")

@bot.event
async def on_message_delete(message):
    global deletedMessage
    if message.author == bot.user:
        return
    rgbColor = discord.Color.from_rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255))

    deletedMessage = discord.Embed(color=rgbColor, description=f"{message.author} deleted a message! \nMessage: {message.content}\nGuild: {message.guild}\nChannel: <#{message.channel.id}>")
    deletedMessage.set_thumbnail(url=message.author.avatar_url)

@bot.command()
async def snipe(ctx):
    if deletedMessage != "":
        await ctx.send(embed=deletedMessage)
    else:
        await ctx.send("Sorry, there hasn't been a message deleted in this discord.")

bot.run("BOT TOKEN")#Place your bot token here.
