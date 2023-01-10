import discord
from discord.ext import commands
import scraper
import os

bot = commands.Bot(command_prefix="$",intents=discord.Intents.all(),case_insensitive=True)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready!")

@bot.command()
async def getidea(ctx):
    ideaScraper = scraper.Scrape()
    ideaTitle, ideaHeader = ideaScraper.RetreiveCodeIdea()
    embed = discord.Embed(title=ideaTitle,description=ideaHeader,url=ideaScraper.url,color=discord.Color.from_rgb(244,224,77))
    bulbFile = discord.File(f"{os.getcwd()}\whattocodefetcher\whattocode.png",filename="Lightbulb.png")
    textFile = discord.File(f"{os.getcwd()}\whattocodefetcher\whattocodetext.png",filename="Text.png")
    embed.set_thumbnail(url="attachment://Text.png")
    embed.set_footer(text=ideaScraper.url,icon_url="attachment://Lightbulb.png")
    await ctx.send(files=[bulbFile,textFile],embed=embed)

bot.run("")
