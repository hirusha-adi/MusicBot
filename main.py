# IMPORTS
# ----------------------------------------------------
import platform
import os
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

from musicbot.web.keep_alive import keep_alive
import musicbot.database.settings.config as config



# CODE STARTS HERE
# ----------------------------------------------------
# |||||||||||||||||
TOKEN = config.BotInfo.BOT_TOKEN
# TOKEN = os.environ['TOKEN']
# |||||||||||||||||

client = commands.Bot(command_prefix=config.BotInfo.BOT_PREFIX)
client.remove_command('help')

# Im using the public, free lava.link servers
client.lava_nodes = [
  {
    'host':"lava.link",
    'port':80,
    'rest_uri':f'http://lava.link:80',
    'identifier':'MAIN',
    'password':'anything',
    'region':'singapore'
  }
]

# Loading all cogs
# ----------------------------
client.load_extension('musicbot.cogs.musiccog')
for filename in os.listdir('musicbot/cogs'):
  if filename.endswith('.py'):
    try:
      client.load_extension(f'musicbot.cogs.{filename[:-3]}')
      print(f"[+] Loaded: musicbot.cogs.{filename[:-3]}")
    except Exception as excl:
      print(f"[+] Unable to load: musicbot.cogs.{filename[:-3]}  :  {excl}")



# Running the flask webserver, please enable this if you are planning to host this on a repl to keep it up using UptimeRobot
# You may enable this if you know what you are doing (with flask) (maybe host a custom website for this thing)
if config.BotInfo.RUN_FLASK_WEB_SERVER:
    keep_alive()

client.run(TOKEN)
