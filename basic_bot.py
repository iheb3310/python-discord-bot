'''discord bot created using the discord.py library'''
import random
import discord
from discord.ext import commands

TOKEN = 'MzYzMDAyODk4NzEzNjczNzI4.DNpXLg.yJq1uAf140ahCyKcpPnJn2mQEio'
BOT = commands.Bot(command_prefix='!')

@BOT.event
async def on_ready():
    '''console output on initialization'''
    print('Logged in as')
    print(BOT.user.name)
    print(BOT.user.id)
    print('------')

@BOT.command()
async def helpme():
    '''outputs list of commands'''
    embed=discord.Embed(title="Commands", description="Current list of commands.", color=0xb70000)
    embed.add_field(name='Add', value='add two numbers together. Example: "!add 12 12"', inline=True)
    embed.add_field(name='Choose', value='pick random from choices given. Example: "!choose eenie meenie minie moe"', inline=True)
    embed.add_field(name='Joined', value='get join date of member. Example: "!joined RedRedemption"', inline=True)
    embed.add_field(name='Repeat', value='get the bot to repeat some input. Example "!repeat I love life', inline=True)
    await BOT.say(embed=embed)

@BOT.command()
async def repeat(*textstring: str):
    '''get the bot to repeat some input'''
    text=' '.join(textstring)
    embed=discord.Embed(color=0xb70000)
    embed.add_field(name='Repeat', value=text, inline=True)
    await BOT.say(embed=embed)

@BOT.command()
async def add(left: int, right: int):
    """Adds two numbers together."""
    text='' + left + ' ' + right
    embed=discord.Embed(color=0xb70000)
    embed.add_field(name='Add', value=text, inline=True)
    await BOT.say(embed=embed)

@BOT.command(description='For when you wanna settle the score some other way')
async def choose(*choices: str):
    """Chooses between multiple choices."""
    text=random.choice(choices)
    embed=discord.Embed(color=0xb70000)
    embed.add_field(name='Choice', value=text, inline=True)
    await BOT.say(embed=embed)

@BOT.command()
async def joined(member: discord.Member):
    """Says when a member joined."""
    text='{0.name} joined in {0.joined_at}'.format(member)
    embed=discord.Embed(color=0xb70000)
    embed.add_field(name='Joined', value=text, inline=True)
    await BOT.say(embed=embed)

BOT.run(str(TOKEN))

# -----------------------------------------
