import discord  # https://guide.pycord.dev/installation/
import json  # for storing data

# declare client
intents = discord.Intents.all()  # was default()
bot = discord.Bot(intents=intents)

# json config data
f = open('config.json', encoding="utf-8")  # open json file
config = json.load(f)  # load file into dict
f.close()  # close file

guild_ids = config["guild_ids"]  # comma separated guild ids
@bot.event
async def on_ready():
    print(f"{bot.user.name} Online.")

@bot.slash_command(description="Archive the current server", guild_ids=guild_ids)
async def copy(ctx):
    pass


# run bot
# discord dev portal -> bot -> reset token -> copy
bot.run(config["token"])