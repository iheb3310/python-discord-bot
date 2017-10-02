'''discord bot created using the discord.py library'''
import os
import random
import requests
import discord
from discord.ext import commands

#--------------API INITIAL/ENDPOINTS---------------------
CLAN_RESPONSE = requests.get('http://api.cr-api.com/clan/2GG9CC', timeout=5.000)
CLAN_RESPONSE = CLAN_RESPONSE.json()
CLAN_MEMBERS = CLAN_RESPONSE['members']
CLAN_MEMBER_DICT = map_clan_member_to_tag()

def map_clan_member_to_tag():
    '''creates dict for clan members names mapped to member tags'''
    res = {}
    for member in CLAN_MEMBERS:
        res[member['name']] = res[member['tag']]
    return res

# -----------------------------------------

TOKEN = os.environ.get('TOKEN')
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
    await BOT.say(
        'Current list of commands...\n'
        'Add: add two numbers together. Example: "!add 12 12"\n'
        'Choose: pick random from choices given. Example: "!choose eenie meenie minie moe"\n'
        'Joined: get join date of member. Example: "!joined RedRedemption"\n'
        'Repeat: get the bot to repeat some input. Example "!repeat I love life\n'
        'Memberlist: return list of all members in Clutchfans. Example "!memberlist"\n'
        '---------------------------------------------------------------------------\n'
        'Regarding Clan Information:\n'
        'Clan information is fetched once per 24 hours.\n'
        )

@BOT.command()
async def repeat(*textstring: str):
    '''get the bot to repeat some input'''
    await BOT.say(' '.join(textstring))

@BOT.command()
async def add(left: int, right: int):
    """Adds two numbers together."""
    await BOT.say(left + right)

@BOT.command(description='For when you wanna settle the score some other way')
async def choose(*choices: str):
    """Chooses between multiple choices."""
    await BOT.say(random.choice(choices))

@BOT.command()
async def joined(member: discord.Member):
    """Says when a member joined."""
    await BOT.say('{0.name} joined in {0.joined_at}'.format(member))

@BOT.command()
async def memberlist():
    """Gets a list of current clanmembers in Clutchfans"""
    res = ""
    for member in CLAN_MEMBERS:
        res += member['name'] + ", "
    await BOT.say(res)

BOT.run(str(TOKEN))
