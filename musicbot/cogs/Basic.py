import discord
import platform
import time
import datetime
from discord.ext import commands
import musicbot.database.settings.config as config


class Basic(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        self.start_time = None

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'[+] Logged in as {self.client.user.name}')
        print(f'[+] [+] Discord.py API version: {discord.__version__}')
        print(f'[+] Python version: {platform.python_version()}')

        self.start_time = time.time()
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"The simple music bot of Z"))

        print('[+] Bot is ready!')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="ERROR", description="`You don't have the permissions required to use this command!`", color=0xff0000)
            embed.set_author(
                name=f"{config.BotInfo.BOT_NAME}", icon_url=f"{config.BotInfo.BOT_AVATAR_URL}")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            await ctx.send(embed=embed)
            return

        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title="Something is wrong!", description="An error has been occured!", color=0xff0000)
            embed.set_author(
                name=f"{config.BotInfo.BOT_NAME}", icon_url=f"{config.BotInfo.BOT_AVATAR_URL}")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed.add_field(
                name="Error", value="You haven't passed the needed arguments for this command to run properly", inline=True)
            embed.add_field(
                name="Possible Fix", value=f"use `{config.BotInfo.BOT_PREFIX}help all` to list out all the command and check the proper usage of the command you used", inline=True)
            await ctx.send(embed=embed)

    @commands.command()
    async def uptime(self, ctx):
        try:
            current_time = time.time()
            difference = int(round(current_time - self.start_time))
            text = str(datetime.timedelta(seconds=difference))
            embed = discord.Embed(color=0xff0000)
            embed.add_field(name="The bot was online for: ",
                            value=f":alarm_clock: {text}", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(
                title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed3.set_author(
                name=f"{config.BotInfo.BOT_NAME}", icon_url=f"{config.BotInfo.BOT_AVATAR_URL}")
            embed3.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed3)

    @commands.command()
    async def creator(self, ctx):
        await ctx.send(f"Bot made by **{config.BotInfo.CREATOR_NAME}**")


def setup(client: commands.Bot):
    client.add_cog(Basic(client))
