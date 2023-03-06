from fasterGetUser import getMC
from discord.ext import commands
import discord
import time

#Just named this the faster bot because it works with the fasterGetUser

intent = discord.Intents.all()
bot = commands.Bot(command_prefix="$",intents=intent)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready.")

@bot.command()
async def mc(ctx,username):
    startTime = time.time()
    getUser = getMC(username).run()
    userJson = getUser[0].json()
    username = userJson['name']
    uuid = userJson['id']
    
    if getUser[0].status_code != 200:
        embed = discord.Embed(description=f"`Can\'t find user: {username}`",color=discord.Color.from_rgb(0,0,0))
        embed.set_footer(text=f"Took {round(time.time() - startTime,2)}s but couldn't find the user.")
    else:
        embed = discord.Embed(title=username,url=f"https://namemc.com/profile/{username}",color=discord.Color.random())
        embed.add_field(name="UUID",value=f"`{uuid}`",inline=True)
        embed.set_thumbnail(url=getUser[-1])
        embed.set_footer(text=f"Retrieved your user in {round(time.time() - startTime,2)}s")

    await ctx.send(embed=embed)

bot.run("")
