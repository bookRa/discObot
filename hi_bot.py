# This example requires the 'message_content' intent.
import os
import discord
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    print(f'recieved message {message}')
    print(f'client.user: {client.user}')
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('sup')

token = os.getenv('SECRET_DISCORD_TOKEN')
client.run(token)
