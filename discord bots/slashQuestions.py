import discord
from discord.ext import commands
import time   
import asyncio

intent = discord.Intents.all()
timeouts = {}

bot = commands.Bot(command_prefix="$",intents=intent)

def removeUserTimeout(user):
    timeouts.pop(user)
    print(f"{user} was taken off timeout.\n{timeouts}")

def createEmbed(user,response,question):
    embed = discord.Embed()
    if response == "cooldown":
        embed.description = f"Please wait before asking another question. You are on cooldown for {int((timeouts[user] - time.time()) / 60)}m."
        embed.color = discord.Color.from_rgb(255,255,102)
        embed.title = "Take a break."
    if response == "success":
        embed.color = discord.Color.from_rgb(124, 223, 124)
        embed.title = "Your question has been asked."
    if response == "question":
        embed.description = question
        embed.color = discord.Color.from_rgb(124, 223, 124)
        embed.title = f"{user} has a question."
        embed.set_thumbnail(url=user.display_avatar.url)
        embed.set_footer(text=f"userID: {user.id}")
    
    return embed

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Im ready")

@bot.tree.command(description="Sends a question in the \"questions\" channel.")
async def ask(interaction: discord.Interaction,question: str):
    userCooldown = 10000
    if interaction.user in timeouts:
        await interaction.response.send_message(embed=createEmbed(interaction.user,"cooldown",question),ephemeral=True)
        return
      
    channel = bot.get_channel()#Pass your questions channel ID in here.
    await interaction.response.send_message(embed=createEmbed(interaction.user,"success",question),ephemeral=True)
    await channel.send(embed=createEmbed(interaction.user,"question",question))

    timeouts[interaction.user] = time.time() + userCooldown
    await asyncio.sleep(userCooldown)
    removeUserTimeout(interaction.user)

bot.run("")#Bot Token goes in here
