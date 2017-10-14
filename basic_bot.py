'''discord bot created using the discord.py library'''
import os
import random
import requests
import discord
from discord.ext import commands

TOKEN = os.environ.get('TOKEN')
BOT = commands.Bot(command_prefix='!')
#--------------API INITIAL/ENDPOINTS---------------------
'''
TEMP DISABLE API CALL.
try:
    CLAN_RESPONSE = requests.get('http://api.cr-api.com/clan/2GG9CC', timeout=5.000)
    CLAN_RESPONSE = CLAN_RESPONSE.json()
    CLAN_MEMBERS = CLAN_RESPONSE['members']
except requests.exceptions.RequestException as e:
    print(e)
'''

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
        'Get member: return data for a member. Example "!member RedRedemption"\n'
        '---------------------------------------------------------------------------\n'
        'Regarding Clan Information:\n'
        'Clan information is fetched once per 24 hours.\n'
        'API to clan data is down, so Memberlist and member commands will not work.'
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

@BOT.command()
async def getmember(membername: str):
    '''Gets member data from given membername'''
    baseurl = 'http://api.cr-api.com/profile/'
    tag = ""
    url = ""
    for member in CLAN_MEMBERS:
        if member['name'].upper() == membername.upper():
            tag = member['tag']
            url = baseurl+tag

    if tag == "":
        await BOT.say("Can't find " + membername + ".")
        return -1

    memberdata = requests.get(url, timeout=5.000)
    memberdata = memberdata.json()
    experience = memberdata['experience']
    stats = memberdata["stats"]
    games = memberdata["games"]

    await BOT.say(
        'Name: ' + memberdata["name"] + "\n" +
        'Current Trophies: ' + str(memberdata["trophies"]) + "\n" +
        'Current Level: ' + str(experience["level"]) + "\n" +
        '----Statistics----\n' +
        'Legendary Trophies: ' + str(memberdata["legendaryTrophies"]) + "\n" +
        'Highest Trophy Count: ' + str(stats["maxTrophies"]) + "\n" +
        'Three Crown Wins: ' + str(stats["threeCrownWins"]) + "\n" +
        'Favorite card: ' + stats["favoriteCard"] + "\n" +
        'Total donations: ' + str(stats["totalDonations"]) + "\n" +
        'Win-Loss-Draw Record: ' + str(games["wins"]) + "-" + str(games["losses"]) + "-" + str(games["draws"]) + "\n" +
        'Win-Loss-Ratio: ' + str(round(games['wins']/games['losses'], 2))
        )

BOT.run(str(TOKEN))

# -----------------------------------------
