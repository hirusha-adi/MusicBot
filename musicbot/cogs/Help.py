import discord
from discord.ext import commands
import musicbot.database.settings.config as config




class Help(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        self.client.remove_command('help')


    @commands.command()
    async def help(self, ctx, subtype="all"):

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
                embed.set_author(name=f"{config.BotInfo.BOT_NAME}", icon_url=f"{config.BotInfo.BOT_AVATAR_URL}")
                embed.add_field(name="Description", value=f"Connect the player to a voice channel", inline=False)
                embed.add_field(name="Aliases", value="con,\nc,\nconnect ", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await ctx.send(embed=embed)
            
            elif subtype in disconnect_wl:
                embed=discord.Embed(title="Disconnect", color=0xff0000)
                embed.set_author(name=f"{config.BotInfo.BOT_NAME}", icon_url=f"{config.BotInfo.BOT_AVATAR_URL}")
                embed.add_field(name="Description", value=f"Disconnect the player to a voice channel", inline=False)
                embed.add_field(name="Aliases", value="dc, \ndisconnect", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await ctx.send(embed=embed)
            
            elif subtype in play_wl:
                embed=discord.Embed(title="Play", color=0xff0000)
                embed.set_author(name=f"{config.BotInfo.BOT_NAME}", icon_url=f"{config.BotInfo.BOT_AVATAR_URL}")
                embed.add_field(name="Description", value=f"Play or add song to queue", inline=False)
                embed.add_field(name="Aliases", value="p, \nplay", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await ctx.send(embed=embed)

            elif subtype in skip_wl:
                embed=discord.Embed(title="Skip", color=0xff0000)
                embed.set_author(name=f"{config.BotInfo.BOT_NAME}", icon_url=f"{config.BotInfo.BOT_AVATAR_URL}")
                embed.add_field(name="Description", value=f"Skip currently playing song", inline=False)
                embed.add_field(name="Aliases", value="skip", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await ctx.send(embed=embed)
            
            elif subtype in pause_wl:
                embed=discord.Embed(title="Pause", color=0xff0000)
                embed.set_author(name=f"{config.BotInfo.BOT_NAME}", icon_url=f"{config.BotInfo.BOT_AVATAR_URL}")
                embed.add_field(name="Description", value=f"Pause the current song", inline=False)
                embed.add_field(name="Aliases", value="pause", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await ctx.send(embed=embed)
            
            elif subtype in resume_wl:
                embed=discord.Embed(title="Resume", color=0xff0000)
                embed.set_author(name=f"{config.BotInfo.BOT_NAME}", icon_url=f"{config.BotInfo.BOT_AVATAR_URL}")
                embed.add_field(name="Description", value=f"Resume the current paused song", inline=False)
                embed.add_field(name="Aliases", value="resume", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await ctx.send(embed=embed)
            
            elif subtype in seek_wl:
                embed=discord.Embed(title="Seek", color=0xff0000)
                embed.set_author(name=f"{config.BotInfo.BOT_NAME}", icon_url=f"{config.BotInfo.BOT_AVATAR_URL}")
                embed.add_field(name="Description", value=f"Seek the music backward or forward", inline=False)
                embed.add_field(name="Aliases", value="seek", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await ctx.send(embed=embed)
            
            elif subtype in vol_wl:
                embed=discord.Embed(title="Volume", color=0xff0000)
                embed.set_author(name=f"{config.BotInfo.BOT_NAME}", icon_url=f"{config.BotInfo.BOT_AVATAR_URL}")
                embed.add_field(name="Description", value=f"Set volume for the music", inline=False)
                embed.add_field(name="Aliases", value="volume, \nvol", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await ctx.send(embed=embed)
            
            elif subtype in loop_wl:
                embed=discord.Embed(title="Loop", color=0xff0000)
                embed.set_author(name=f"{config.BotInfo.BOT_NAME}", icon_url=f"{config.BotInfo.BOT_AVATAR_URL}")
                embed.add_field(name="Description", value=f"Set loop to `NONE`, `CURRENT` or `PLAYLIST`", inline=False)
                embed.add_field(name="Aliases", value="loop", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await ctx.send(embed=embed)
            
            elif subtype in nowplaying_wl:
                embed=discord.Embed(title="Now Playing", color=0xff0000)
                embed.set_author(name=f"{config.BotInfo.BOT_NAME}", icon_url=f"{config.BotInfo.BOT_AVATAR_URL}")
                embed.add_field(name="Description", value=f"What's playing now?", inline=False)
                embed.add_field(name="Aliases", value="nowplaying \nnp", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await ctx.send(embed=embed)
            
            
            elif subtype in queue_wl:
                embed=discord.Embed(title="Queue", color=0xff0000)
                embed.set_author(name=f"{config.BotInfo.BOT_NAME}", icon_url=f"{config.BotInfo.BOT_AVATAR_URL}")
                embed.add_field(name="Description", value=f"Bot's current queue", inline=False)
                embed.add_field(name="Aliases", value="queue \nq", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await ctx.send(embed=embed)
            
            elif subtype in equalizer_wl:
                embed=discord.Embed(title="Equalizer", color=0xff0000)
                embed.set_author(name=f"{config.BotInfo.BOT_NAME}", icon_url=f"{config.BotInfo.BOT_AVATAR_URL}")
                embed.add_field(name="Description", value=f"Set equalizer", inline=False)
                embed.add_field(name="Aliases", value="equalizer \neq", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await ctx.send(embed=embed)

            else:
                embed=discord.Embed(title="Help", color=0xff0000)
                embed.set_author(name=f"{config.BotInfo.BOT_NAME}", icon_url=f"{config.BotInfo.BOT_AVATAR_URL}")
                embed.add_field(name="Music", value=f"`{config.BotInfo.BOT_PREFIX}connect` - Connect to Voice Channel \n`{config.BotInfo.BOT_PREFIX}disconnect` - Disconnect bot from Voice Channel \n`{config.BotInfo.BOT_PREFIX}play [song-name/link]` - Play the song \n`{config.BotInfo.BOT_PREFIX}skip` - Skip the currently playing song \n`{config.BotInfo.BOT_PREFIX}pause` - Pause the music \n`{config.BotInfo.BOT_PREFIX}resume` - Resume the music \n`{config.BotInfo.BOT_PREFIX}seek [seconds]` - Skip the given seconds of the playing song \n`{config.BotInfo.BOT_PREFIX}volume [number]` - Change the volume of the song \n`{config.BotInfo.BOT_PREFIX}loop [type]` - Play music in a loop \n`{config.BotInfo.BOT_PREFIX}nowplaying` - Show the song which is being played right now \n`{config.BotInfo.BOT_PREFIX}queue` - Diplay the songs waiting to be played \n`{config.BotInfo.BOT_PREFIX}equalizer` - Maybe tune the song to your liking?", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await ctx.send(embed=embed)

        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed3.set_author(name=f"{config.BotInfo.BOT_NAME}", icon_url=f"{config.BotInfo.BOT_AVATAR_URL}")
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed3)



def setup(client: commands.Bot):
    client.add_cog(Help(client))
