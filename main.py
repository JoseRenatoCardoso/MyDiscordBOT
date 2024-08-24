import discord
import os

intents = discord.Intents.default()
intents.messages = True  # Enable the intent to receive messages

client = discord.Client(intents=intents)

@client.event
async def on_ready(): #Registra que o BOT está online
    print('Hey, {0.user} just appeared'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await message.channel.send('I received your message!')


client.run(os.getenv('DTOKEN'))