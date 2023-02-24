import discord
from discord.ext import commands

intent = discord.Intents.all()

bot = commands.Bot(command_prefix="$",intents=intent)

async def channel_autocomplete(interaction: discord.Interaction, channel_id):
    completions = {channels.name:channels.id for channels in interaction.guild.voice_channels}

    return [discord.app_commands.Choice(name=channel,value=str(channelID)) for channel,channelID in completions.items()]

@bot.tree.command(description="Tags any given voice channel.")
@discord.app_commands.autocomplete(channel_id=channel_autocomplete)
async def tagchannel(interaction: discord.Interaction, channel_id: str):
    choices = await channel_autocomplete(interaction,channel_id)

    if channel_id not in str(choices):
        errorEmbed = discord.Embed(title="Please choose an autocompleted choice.",description=f"`{channel_id} is not a valid choice!`",color=discord.Color.from_rgb(255,255,255))
        await interaction.response.send_message(embed=errorEmbed)
        return

    await interaction.response.send_message(f"<#{channel_id}>\n`<#{channel_id}>`")

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Im ready")

bot.run("")
