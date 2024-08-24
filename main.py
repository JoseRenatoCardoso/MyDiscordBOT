import discord
import os
from discord.ext import commands

# Set up intents
intents = discord.Intents.default()
intents.messages = True
intents.members = True

# Create a Bot that uses a '!' prefix
MyBOT = commands.Bot(command_prefix='!', intents=intents)

@MyBOT.event
async def on_ready():
    # Print a message when the bot is online
    print(f'Hey, {MyBOT.user} just appeared')

@MyBOT.event
async def on_message(message):
    # Bot does not respond to its own messages
    if message.author == MyBOT.user:
        return
    # Respond to all messages
    await message.channel.send('I received your message!')

# Run the bot
MyBOT.run(os.getenv('DTOKEN'))
