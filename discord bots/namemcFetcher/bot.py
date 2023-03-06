from getUser import getMC
from discord.ext import commands
import discord
import time

#Works with the slower getUser

intent = discord.Intents.all()
bot = commands.Bot(command_prefix="$",intents=intent)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready.")

@bot.command()
async def mc(ctx,username):
    startTime = time.time()
    user = getMC().getHTML(username)
    
    if type(user) == tuple:
        description = "\n".join(user[0])
        embed = discord.Embed(title=user[1],url=user[2],color=discord.Color.random())
        embed.add_field(name="UUID",value=f"`{description}`",inline=True)
        embed.set_thumbnail(url=user[-1])
        embed.set_footer(text=f"Retrieved your user in {round(time.time() - startTime,2)}s")
    else:
        embed = discord.Embed(description=user,color=discord.Color.from_rgb(0,0,0))
        embed.set_footer(text=f"Took {round(time.time() - startTime,2)}s but couldn't find the user.")

    await ctx.send(embed=embed)

bot.run("")
