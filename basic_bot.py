'''discord bot created using the discord.py library'''

# pylint: disable=W0612

import random
import json
import discord
from discord.ext import commands

def initiate_bot():

    ''' Initiate bot loop '''

    with open("token.txt", "r") as readfile:
        token = readfile.read().strip()
    bot = commands.Bot(command_prefix='!')

    @bot.event
    async def on_ready():
        '''console output on initialization'''
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('------')

    @bot.command()
    async def helpme():
        '''outputs list of commands'''
        help_text = 'get list of commands. Example: "!helpme"'
        add_text = 'add two numbers together. Example: "!add 12 12"'
        subtract_text = 'subtract two numbers. Example: "!subtract 12 2"'
        multiply_text = 'multiply two numbers together. Example: "!multiply 4 3"'
        divide_text = 'divide two numbers. Example: "!divide 6 2"'
        choose_text = 'pick random from choices given. Example: "!choose eenie meenie minie moe"'
        repeat_text = 'get the bot to repeat some input. Example "!repeat I love life'
        addquote_text = 'add quote to database. Example: "!addquote This is a quote.'
        getquote_text = 'gets random quote from database. Example: "!getquote"'

        embed = discord.Embed(title="Commands", description="Current list of commands.")
        embed.add_field(name='Help', value=help_text, inline=True)
        embed.add_field(name='Add', value=add_text, inline=True)
        embed.add_field(name='Subtract', value=subtract_text, inline=True)
        embed.add_field(name='Multiply', value=multiply_text, inline=True)
        embed.add_field(name='Divide', value=divide_text, inline=True)
        embed.add_field(name='Choose', value=choose_text, inline=True)
        embed.add_field(name='Repeat', value=repeat_text, inline=True)
        embed.add_field(name='Add Quote', value=addquote_text, inline=True)
        embed.add_field(name='Get Quote', value=getquote_text, inline=True)
        await bot.say(embed=embed)

    @bot.command()
    async def repeat(*textstring: str):
        '''get the bot to repeat some input'''
        text = ' '.join(textstring)
        embed = discord.Embed()
        embed.add_field(name='Repeat', value=text, inline=True)
        await bot.say(embed=embed)

    @bot.command()
    async def add(left: float, right: float):
        """Adds two numbers together."""
        text = str(left+right)
        embed = discord.Embed()
        embed.add_field(name='Add', value=text, inline=True)
        await bot.say(embed=embed)

    @bot.command()
    async def subtract(left: float, right: float):
        ''' Subtracts two numbers '''
        text = str(left-right)
        embed = discord.Embed()
        embed.add_field(name='Subtract', value=text, inline=True)
        await bot.say(embed=embed)

    @bot.command()
    async def multiply(left: float, right: float):
        ''' Multiplies two numbers '''
        text = str(left*right)
        embed = discord.Embed()
        embed.add_field(name='Multiply', value=text, inline=True)
        await bot.say(embed=embed)

    @bot.command()
    async def divide(left: float, right: float):
        ''' Divides two numbers '''
        text = str(left/right)
        embed = discord.Embed()
        embed.add_field(name='Divide', value=text, inline=True)
        await bot.say(embed=embed)

    @bot.command()
    async def choose(*choices: str):
        """Chooses between multiple choices."""
        text = random.choice(choices)
        embed = discord.Embed()
        embed.add_field(name='Choice', value=random.choice(choices), inline=True)
        await bot.say(embed=embed)

    @bot.command()
    async def addquote(*textstring: str):
        '''Adds quote to list of quotes.'''
        quotes = {}
        with open('quotes.json', 'r') as readfile:
            quotes = json.load(readfile)
            quote_list = quotes['quote_list']

        quotes['quote_list'].append(textstring)

        with open('quotes.json', 'w') as outfile:
            json.dump(quotes, outfile)

        text = "Quote added to database."
        embed = discord.Embed()
        embed.add_field(name='Add Quote', value=text, inline=True)
        await bot.say(embed=embed)

    @bot.command()
    async def getquote():
        ''' Gets quote from database. '''
        text = ''
        with open('quotes.json', 'r') as readfile:
            quotes = json.load(readfile)
            quote_list = quotes['quote_list']
            text = quote_list[random.randint(0, len(quote_list)-1)]

        text = text.join(' ')
        embed = discord.Embed()
        embed.add_field(name='Get Quote', value=text, inline=True)
        await bot.say(embed=embed)

    bot.run(token)

def main():

    ''' Program driver '''

    initiate_bot()

if __name__ == '__main__':
    main()
