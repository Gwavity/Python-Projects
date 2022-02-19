import discord

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("I'm ready")
    guild = #Place the guildID that you would like to remove all bans from
    await unbanAll(guild)

async def unbanAll(guild):
    getGuild = client.get_guild(guild)
    getbans = await getGuild.bans()
    for i in getbans:
        await getGuild.unban(i.user)

client.run("")
