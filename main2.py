import discord, platform, time, os, json
from discord.ext import commands
from keep_alive import keep_alive

try:
    if platform.system().lower().startswith('win'):
        os.system("pip3 install discord.py")
        os.system("pip3 install dismusic")
        os.system("pip3 install discord-custom-help")
    else:
        os.system("pip install discord.py")
        os.system("pip install dismusic==1.0.1")
        os.system("pip install discord-custom-help")
except:
  print("Error")

# token = os.environ['TOKEN']
botconfigdata = json.load(open("config.json", "r"))
bot_prefix = botconfigdata["prefix"]
token = botconfigdata["token"]

bot = commands.Bot(command_prefix=bot_prefix)
# bot.remove_command('help')

try:
  print("connectin")
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
  print("connected")
except Exception as e:
  print(e)
  

start_time = None

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print(f'Discord.py API version: {discord.__version__}')
    print(f'Python version: {platform.python_version()}')

    global start_time
    start_time = time.time()

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} servers!"))
    print('Bot is ready!')

    bot.load_extension('dismusic')
    bot.load_extension('dch')

# keep_alive()
bot.run(token)