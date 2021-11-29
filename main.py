import os
from dotenv import load_dotenv
from nextcord.ext import commands
import vardata

load_dotenv()

# Define the bot
command_prefix = vardata.COMMANDPREFIX  # Importing command prefix from variables file
client = commands.Bot(command_prefix=command_prefix)  # Setting bot's command prefix
client.remove_command('help')


@client.event  # Bot reports that it is online
async def on_ready():
    print('{0.user} has marched into battle!'.format(client))


@client.event  # Catches command formatting errors
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('You must input your command in the correct format!')


@client.event  # Helps users figure out how to call the bot
async def on_message(message):
    if message.author == client.user:
        return
    elif message.author.bot:
        return
    elif client.user.mentioned_in(message) and message.mention_everyone is False:
        await message.reply(f'You can access my commands with {command_prefix}help')
    await client.process_commands(message)

# Initialization
for folder in os.listdir("modules"):  # Loads all the commands
    if os.path.exists(os.path.join("modules", folder, "cog.py")):
        client.load_extension(f"modules.{folder}.cog")


client.run(os.getenv('SABATONHISTORY_TOKEN'))  # Runs the bot token to activate
