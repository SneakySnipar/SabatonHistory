from nextcord.ext import commands


class Ping(commands.Cog, name="Ping"):
    """Check the bot's latency"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        latency = self.bot.latency
        latency = round(latency * 1000)
        await ctx.send(f'Pong! My response time is currently {latency}ms')


def setup(bot: commands.Bot):
    bot.add_cog(Ping(bot))
