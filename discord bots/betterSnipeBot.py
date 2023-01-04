import discord
from discord.ext import commands
import asyncio

intent = discord.Intents.all()
bot = commands.Bot(command_prefix="$",intents=intent)
deletedMessages = {}

@bot.event
async def on_ready():
    print("I'm ready")

def deleteEmbed(currentMessage,pos,guildID):
    embed = discord.Embed(title="Sniped Messages!",color=discord.Color.from_rgb(0,0,0))
    embed.set_thumbnail(url=currentMessage[0].display_avatar.url)
    embed.add_field(name="User: ",value=currentMessage[0].name,inline=False)
    embed.add_field(name="Message: ",value=currentMessage[1],inline=False)
    embed.add_field(name="Channel: ",value=f"<#{currentMessage[-1].id}>",inline=False)
    embed.set_footer(text=f"Page #{pos + 1}/{len(deletedMessages[guildID])}")
    return embed

class Menu(discord.ui.View):
    def __init__(self,author):
        super().__init__(timeout=None)
        self.pos = 0
        self.author = author

    async def increasePos(self,guild):
        self.pos += 1
        if self.pos >= len(deletedMessages[guild]):
            self.pos = 0

    async def decreasePos(self,guild):
        self.pos -= 1
        if self.pos < 0:
            self.pos = len(deletedMessages[guild]) - 1

    @discord.ui.button(label="<",style=discord.ButtonStyle.grey,custom_id="persistent_BackArrow")
    async def backArrow(self,interaction: discord.Interaction,button:discord.ui.Button):
        await self.decreasePos(interaction.guild.id)
        currentMessage = deletedMessages[interaction.guild.id][self.pos]
    
        await interaction.message.edit(embed=deleteEmbed(currentMessage,self.pos,interaction.guild.id))
        await interaction.response.defer()

    @discord.ui.button(label=">",style=discord.ButtonStyle.grey,custom_id="persistent_ForwardArrow")
    async def forwardArrow(self,interaction: discord.Interaction,button:discord.ui.Button):
        await self.increasePos(interaction.guild.id)
        currentMessage = deletedMessages[interaction.guild.id][self.pos]

        await interaction.message.edit(embed=deleteEmbed(currentMessage,self.pos,interaction.guild.id))
        await interaction.response.defer()
    
    @discord.ui.button(label="Delete!",style=discord.ButtonStyle.red,custom_id="persistent_DeleteButton")
    async def deleteButton(self,interaction: discord.Interaction, button: discord.ui.Button):
        deletionEmbed = discord.Embed(title="Deleting Sniped Messages shortly.",color=discord.Color.from_rgb(0,0,0))
        if interaction.user == self.author:
            await interaction.response.send_message(embed=deletionEmbed,ephemeral=True)
            await asyncio.sleep(3)
            await interaction.message.delete()

@bot.command()
async def snipe(ctx):
    if ctx.guild.id in deletedMessages:
        currentMessage = deletedMessages[ctx.guild.id][0]

        await ctx.send(embed=deleteEmbed(currentMessage,0,ctx.guild.id),view=Menu(ctx.message.author))#Sends the deleted message content
    else:
        await ctx.send("There hasnt been a deleted message in your guild.")

@bot.event
async def on_message_delete(message):#Gets every deleted message.
    global deletedMessages#Updates "deletedMessage" everytime a user deletes their message
    if len(message.embeds) >= 1:
        return
    if message.guild.id not in deletedMessages:
        deletedMessages[message.guild.id] = [[message.author,message.content,message.channel]]
    else:
        if len(deletedMessages[message.guild.id]) >= 3:
            deletedMessages[message.guild.id].pop(0)

        deletedMessages[message.guild.id].append([message.author,message.content,message.channel])

bot.run("TOKEN")
