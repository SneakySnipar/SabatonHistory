from nextcord.ext import commands
import youtube_dl


class MusicPlayer(commands.Cog, name="Music"):
    """Receives music commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Music Player Section
    @commands.command()
    async def play(self, ctx, url):
        """Queues up a song and has the bot join a channel, format: play (url)"""

        if ctx.author.voice is None:
            await ctx.send('You are not currently connected to a voice channel')
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

        ctx.voice_client.stop()
        vc = ctx.voice_client
        ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                          'options': '-vn'
                          }
        ydl_options = {'format': 'bestaudio/best',
                       'postprocessors': [{
                           'key': 'FFmpegExtractAudio',
                           'preferredcodec': 'mp3',
                           'preferredquality': '192',
                       }]
                       }

        with youtube_dl.YoutubeDL(ydl_options) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            import nextcord
            source = await nextcord.FFmpegOpusAudio.from_probe(url2, **ffmpeg_options)
            vc.play(source)
            await ctx.send('Now playing your selected song!')

    @commands.command()
    async def stop(self, ctx):
        """Stops the music and disconnects the bot"""
        ctx.voice_client.stop()
        await ctx.voice_client.disconnect()
        await ctx.send('Disconnecting...')

    @commands.command()
    async def pause(self, ctx):
        """Pauses the current song"""
        await ctx.send('Music has been paused.')
        await ctx.voice_client.pause()

    @commands.command()
    async def resume(self, ctx):
        """Resumes the current song"""
        await ctx.send('Music has been resumed.')
        await ctx.voice_client.resume()


def setup(bot: commands.Bot):
    bot.add_cog(MusicPlayer(bot))
