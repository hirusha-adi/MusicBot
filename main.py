import platform, time, os, json, datetime

try:
    import discord
    from discord.ext import commands
except:
    if platform.system().lower().startswith('win'):
            os.system("pip3 install discord.py")
    else:
            os.system("pip install discord.py")
    import discord
    from discord.ext import commands


botconfigdata = json.load(open("config.json", "r"))
bot_prefix = botconfigdata["prefix"]
bot_cretor = botconfigdata["creator"]
bot_name = botconfigdata["bot-name"]
bot_av = botconfigdata["bot-av-url"]
bp = bot_prefix
token = botconfigdata["token"]

bot = commands.Bot(command_prefix=bot_prefix)
bot.remove_command('help')

bot.lava_nodes = [
  {
    'host':"lava.link",
    'port':80,
    'rest_uri':f'http://lava.link:80',
    'identifier':'MAIN',
    'password':'anything',
    'region':'singapore'
  }
]


start_time = None


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print(f'Discord.py API version: {discord.__version__}')
    print(f'Python version: {platform.python_version()}')

    global start_time
    start_time = time.time()

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"The simple music streaming bot"))
    print('Bot is ready!')

    bot.load_extension('musiccog')


@bot.command()
async def help(ctx, subtype="all"):

    try:
        connect_wl = ("con", "c", "connect")
        disconnect_wl = ("disconnect", "dc", "dis", "d")
        play_wl = ("play", "p")
        skip_wl = ("skip", "next")
        pause_wl = ("pause", "pau")
        resume_wl = ("resume", "res")
        seek_wl = ("forward", "seek")
        vol_wl = ("vol", "volume")
        loop_wl = ("loop", "againnagain", "loops", "mloop")
        nowplaying_wl = ("now", "nowplaying", "current", "np")
        queue_wl = ("queue", "q")
        equalizer_wl = ("equalizer", "eq")

        if subtype in connect_wl:
            embed=discord.Embed(title="Connect", color=0xff0000)
            embed.set_author(name=f"{bot_name}", icon_url=f"{bot_av}")
            embed.add_field(name="Description", value=f"Connect the player to a voice channel", inline=False)
            embed.add_field(name="Aliases", value="con,\nc,\nconnect ", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)
        
        elif subtype in disconnect_wl:
            embed=discord.Embed(title="Disconnect", color=0xff0000)
            embed.set_author(name=f"{bot_name}", icon_url=f"{bot_av}")
            embed.add_field(name="Description", value=f"Disconnect the player to a voice channel", inline=False)
            embed.add_field(name="Aliases", value="dc, \ndisconnect", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)
        
        elif subtype in play_wl:
            embed=discord.Embed(title="Play", color=0xff0000)
            embed.set_author(name=f"{bot_name}", icon_url=f"{bot_av}")
            embed.add_field(name="Description", value=f"Play or add song to queue", inline=False)
            embed.add_field(name="Aliases", value="p, \nplay", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)
        
        elif subtype in skip_wl:
            embed=discord.Embed(title="Skip", color=0xff0000)
            embed.set_author(name=f"{bot_name}", icon_url=f"{bot_av}")
            embed.add_field(name="Description", value=f"Skip currently playing song", inline=False)
            embed.add_field(name="Aliases", value="skip", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)
        
        elif subtype in pause_wl:
            embed=discord.Embed(title="Pause", color=0xff0000)
            embed.set_author(name=f"{bot_name}", icon_url=f"{bot_av}")
            embed.add_field(name="Description", value=f"Pause the current song", inline=False)
            embed.add_field(name="Aliases", value="pause", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)
        
        elif subtype in resume_wl:
            embed=discord.Embed(title="Resume", color=0xff0000)
            embed.set_author(name=f"{bot_name}", icon_url=f"{bot_av}")
            embed.add_field(name="Description", value=f"Resume the current paused song", inline=False)
            embed.add_field(name="Aliases", value="resume", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)
        
        elif subtype in seek_wl:
            embed=discord.Embed(title="Seek", color=0xff0000)
            embed.set_author(name=f"{bot_name}", icon_url=f"{bot_av}")
            embed.add_field(name="Description", value=f"Seek the music backward or forward", inline=False)
            embed.add_field(name="Aliases", value="seek", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)
        
        elif subtype in vol_wl:
            embed=discord.Embed(title="Volume", color=0xff0000)
            embed.set_author(name=f"{bot_name}", icon_url=f"{bot_av}")
            embed.add_field(name="Description", value=f"Set volume for the music", inline=False)
            embed.add_field(name="Aliases", value="volume, \nvol", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)
        
        elif subtype in loop_wl:
            embed=discord.Embed(title="Loop", color=0xff0000)
            embed.set_author(name=f"{bot_name}", icon_url=f"{bot_av}")
            embed.add_field(name="Description", value=f"Set loop to `NONE`, `CURRENT` or `PLAYLIST`", inline=False)
            embed.add_field(name="Aliases", value="loop", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)
        
        elif subtype in nowplaying_wl:
            embed=discord.Embed(title="Now Playing", color=0xff0000)
            embed.set_author(name=f"{bot_name}", icon_url=f"{bot_av}")
            embed.add_field(name="Description", value=f"What's playing now?", inline=False)
            embed.add_field(name="Aliases", value="nowplaying \nnp", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)
        
        
        elif subtype in queue_wl:
            embed=discord.Embed(title="Queue", color=0xff0000)
            embed.set_author(name=f"{bot_name}", icon_url=f"{bot_av}")
            embed.add_field(name="Description", value=f"Bot's current queue", inline=False)
            embed.add_field(name="Aliases", value="queue \nq", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)
        
        elif subtype in equalizer_wl:
            embed=discord.Embed(title="Equalizer", color=0xff0000)
            embed.set_author(name=f"{bot_name}", icon_url=f"{bot_av}")
            embed.add_field(name="Description", value=f"Set equalizer", inline=False)
            embed.add_field(name="Aliases", value="equalizer \neq", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)

        else:
            embed=discord.Embed(title="Help", color=0xff0000)
            embed.set_author(name=f"{bot_name}", icon_url=f"{bot_av}")
            embed.add_field(name="Music", value=f"`{bp}connect` - Connect to Voice Channel \n`{bp}disconnect` - Disconnect bot from Voice Channel \n`{bp}play [song-name/link]` - Play the song \n`{bp}skip` - Skip the currently playing song \n`{bp}pause` - Pause the music \n`{bp}resume` - Resume the music \n`{bp}seek [seconds]` - Skip the given seconds of the playing song \n`{bp}volume [number]` - Change the volume of the song \n`{bp}loop [type]` - Play music in a loop \n`{bp}nowplaying` - Show the song which is being played right now \n`{bp}queue` - Diplay the songs waiting to be played \n`{bp}equalizer` - Maybe tune the song to your liking?", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)

    except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name=f"{bot_name}", icon_url=f"{bot_av}")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed3)


@bot.command()
async def uptime(ctx):

  try:
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(datetime.timedelta(seconds=difference))
    embed=discord.Embed(color=0xff0000)
    embed.add_field(name="The bot was online for: ", value=f":alarm_clock: {text}", inline=False)
    embed.set_footer(text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)
  
  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name=f"{bot_name}", icon_url=f"{bot_av}")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed3)


@bot.command()
async def creator(ctx):
    ctx.send(f"Bot made by **{bot_cretor}**")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed=discord.Embed(title="ERROR", description="`You don't have the permissions required to use this command!`", color=0xff0000)
        embed.set_author(name=f"{bot_name}", icon_url=f"{bot_av}")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        await ctx.send(embed=embed)
        return

    if isinstance(error, commands.MissingRequiredArgument):
        embed=discord.Embed(title="Something is wrong!", description="An error has been occured!", color=0xff0000)
        embed.set_author(name=f"{bot_name}", icon_url=f"{bot_av}")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed.add_field(name="Error", value="You haven't passed the needed arguments for this command to run properly", inline=True)
        embed.add_field(name="Possible Fix", value=f"use `{bot_prefix}help all` to list out all the command and check the proper usage of the command you used", inline=True)
        await ctx.send(embed=embed)
        return


bot.run(token)
