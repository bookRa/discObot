# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.

# This example requires the 'message_content' intent.
import os
from os.path import join, dirname

import discord
from discord.ext import commands

from dotenv import load_dotenv
from gpt import generate_text

# pull env vars from the .env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
TOKEN = os.getenv('SECRET_DISCORD_TOKEN')
print(TOKEN)

intents = discord.Intents.default()
intents.message_content = True

disco = commands.Bot(command_prefix='$', intents=intents)


@disco.event
async def on_ready():
    print(f'We have logged in as {disco.user}')


@disco.command()
async def snap(ctx, arg1, arg2):
    await ctx.send(f'still working on that ^_^;')

@disco.command()
async def lyrics(ctx: commands.Context, lyrics):
    prompts = generate_text(lyrics)
    await ctx.reply(f'pass these into midjourney, bitch: {prompts}')

@disco.command()
async def echo(ctx: commands.Context , arg):
    print('got an echo!')
    og_msg = ctx.message.reference
    if og_msg:
        og_id = og_msg.message_id
        oldie = await ctx.channel.fetch_message(og_id)
        print(f'the old message is {oldie}')
        await ctx.reply(f'{oldie.content}\n{arg}')

    else:
        await ctx.reply(f'*silence*\n{arg}')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    disco.run(TOKEN)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
