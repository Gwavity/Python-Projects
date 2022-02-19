import discord

intent = discord.Intents.all()
client = discord.Client(intents=intent)
newNick = "usersName"

@client.event
async def on_ready():
    print("Im ready")
    guild = client.guilds
    for i in guild:
        members = i.members
        for l in members:
            try:
                # if l.id == Your User Id(ex. 1234567890): #Can be used if you don't want the bot to change a certain users name.
                #     continue
                await l.edit(nick=newNick)
                print(l, "name was changed")
            except Exception as e:
                print(f"{l} | {e} ")#If the bot doesn't have permission to change the current users name then it prints out the error.
                continue
        print("Done")

client.run("BOT TOKEN")#Place your bots token here and run the file. 
