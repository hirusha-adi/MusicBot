import discord
import os
import asyncio
from discord.ext import commands


class CustomPlay(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    async def list(self, ctx):

        all_list = ""
        for file_name in os.listdir("musicbot/database/music"):
            all_list += f"\n{file_name}"
            print(all_list)

        await ctx.send(f"```{all_list}```")

    @commands.command()
    async def cus_play(self, ctx):
        user = ctx.message.author
        voice_channel = user.voice.voice_channel
        channel = None
        # only play music if user is in a voice channel
        if voice_channel != None:
            # grab user's voice channel
            channel = voice_channel.name
            await self.client.say('User is in channel: ' + channel)
            # create StreamPlayer
            vc = await self.client.join_voice_channel(voice_channel)
            player = vc.create_ffmpeg_player(
                'musicbot/database/music/test.mp3', after=lambda: print('done'))
            player.start()
            while not player.is_done():
                await asyncio.sleep(1)
            # disconnect after the player has finished
            player.stop()
            await vc.disconnect()
        else:
            await self.client.say('User is not in a channel.')


def setup(client: commands.Bot):
    client.add_cog(CustomPlay(client))
