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
    await ctx.send(f'still working on that ^_^;')

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

disco.run(TOKEN)
