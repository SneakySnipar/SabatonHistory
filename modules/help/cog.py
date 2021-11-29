import nextcord
from nextcord.ext import commands
from nextcord.errors import Forbidden
import vardata


async def send_embed(ctx, embed):
    try:
        await ctx.send(embed=embed)
    except Forbidden:
        try:
            await ctx.send("Hey, seems like I can't send embeds. Please check my permissions :)")
        except Forbidden:
            await ctx.author.send(
                f"Hey, seems like I can't send any message in {ctx.channel.name} on {ctx.guild.name}\n"
                f"May you inform the server team about this issue? :slight_smile: ", embed=embed)


class Help(commands.Cog):
    """Sends this help message"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, *input):
        """Shows all modules of the bot"""
        prefix = vardata.COMMANDPREFIX
        version = vardata.VERSION
        author = vardata.AUTHOR
        github = vardata.GITHUB

        if not input:
            emb = nextcord.Embed(title='Commands and modules', color=nextcord.Color.blue(),
                                 description=f'Use `{prefix}help <module>` to gain more information about that module '
                                             f':smiley:\n')

            # iterating through cogs, gathering descriptions
            cogs_desc = ''
            for cog in self.bot.cogs:
                cogs_desc += f'`{cog}` {self.bot.cogs[cog].__doc__}\n'

            # adding 'list' of cogs to embed
            emb.add_field(name='Modules', value=cogs_desc, inline=False)

            # integrating through uncategorized commands
            commands_desc = ''
            for command in self.bot.walk_commands():
                # if cog not in a cog
                # listing command if cog name is None and command isn't hidden
                if not command.cog_name and not command.hidden:
                    commands_desc += f'{command.name} - {command.help}\n'

            # adding those commands to embed
            if commands_desc:
                emb.add_field(name='Not belonging to a module', value=commands_desc, inline=False)

            # setting information about author
            emb.add_field(name="About", value=f"""This bot is developed and maintained by {author}\n\
            Coded based on the nextcord.py API\nPlease visit {github} to submit ideas or bugs.""")
            emb.set_footer(text=f"This bot is currently on version {version}.")

        # block called when one cog-name is given
        # trying to find matching cog and it's commands
        elif len(input) == 1:

            # iterating through cogs
            for cog in self.bot.cogs:
                # check if cog is the matching one
                if cog.lower() == input[0].lower():

                    # making title - getting description from doc-string below class
                    emb = nextcord.Embed(title=f'{cog} - Commands', description=self.bot.cogs[cog].__doc__,
                                         color=nextcord.Color.green())

                    # getting commands from cog
                    for command in self.bot.get_cog(cog).get_commands():
                        # if cog is not hidden
                        if not command.hidden:
                            emb.add_field(name=f"`{prefix}{command.name}`", value=command.help, inline=False)
                    # found cog - breaking loop
                    break

            # if input not found
            # yes, for-loops have an else statement, it's called when no 'break' was issued
            else:
                emb = nextcord.Embed(title="What's that?!",
                                     description=f"I've never heard from a module called `{input[0]}` before :scream:",
                                     color=nextcord.Color.orange())

        # too many cogs requested - only one at a time allowed
        elif len(input) > 1:
            emb = nextcord.Embed(title="That's too much.",
                                 description="Please request only one module at once :sweat_smile:",
                                 color=nextcord.Color.orange())

        else:
            emb = nextcord.Embed(title="It's a magical place.",
                                 description="I don't know how you got here. But I didn't see this coming at all.\n"
                                             "Would you please be so kind to report that issue to me on github?\n"
                                             f"{github}\n"
                                             "Thank you! -Sneaky",
                                 color=nextcord.Color.red())

        # sending reply embed using our own function defined above
        await send_embed(ctx, emb)


def setup(bot):
    bot.add_cog(Help(bot))
