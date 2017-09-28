'''discord bot created using the discord.py library'''
import os
import logging
import random
import discord
from discord.ext import commands

TOKEN = os.environ.get('TOKEN')

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# ----------------------------------------

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def helpme():
    '''outputs list of commands'''
    await bot.say(
        'Current list of commands...\n'
        'Add: add two numbers together. Example: "!add 12 12"\n'
        'Choose: pick random from choices given. Example: "!choose eenie meenie minie moe"\n'
        'Joined: get join date of member. Example: "!joined RedRedemption"'
        'Repeat: get the bot to repeat some input. Example "!repeat I love life'
        )

@bot.command()
async def repeat(*textstring : str):
    res = ''
    for text in textstring:
        res += " " + text
    await bot.say(res)

@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))

@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

bot.run(str(TOKEN))
