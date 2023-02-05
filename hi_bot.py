# This example requires the 'message_content' intent.
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('SECRET_DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

disco = commands.Bot(command_prefix='$', intents=intents)


@disco.event
async def on_ready():
    print(f'We have logged in as {disco.user}')


@disco.command()
async def snap(ctx, arg1, arg2):
    print(f'looks like we received something {ctx}')
    print(f'looks like we received something {arg1}')
    print(f'looks like we received something {arg2}')
    await ctx.send(f'you passed {arg1} and {arg2}')



disco.run(TOKEN)
