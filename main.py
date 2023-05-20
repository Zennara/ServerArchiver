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
async def archive(ctx):
    # thinking message
    await ctx.defer()

    # loop through server categories
    for category in ctx.guild.categories:
        # loop through channels in category
        for channel in category.channels:
            # add archived permissions
            await channel.set_permissions(ctx.guild.default_role,
                                          send_messages=False,
                                          add_reactions=False,
                                          send_messages_in_threads=False,
                                          create_public_threads=False,
                                          create_private_threads=False,
                                          connect=False,
                                          create_instant_invite=False,
                                          use_application_commands=False)

    # confirmation message
    await ctx.followup.send(content="Server successfully archived.")


# run bot
# discord dev portal -> bot -> reset token -> copy
bot.run(config["token"])
