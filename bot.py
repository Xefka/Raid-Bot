import discord
import os
from discord.ext import commands
import discord.utils
import datetime
import asyncio
import json


def get_prefix(bot, message):
    prefixes = ['/', 'r$']

    if not message.guild:
        return '?'

    return commands.when_mentioned_or(*prefixes)(bot, message)

client = commands.Bot(command_prefix = get_prefix)

# client.remove_command("help")

@client.event
async def on_ready():
    print(client.user.name + ' has connected to Discord!')
    print('ID : [' + str(client.user.id) + ']')
    with open('logs/log.txt', 'a') as f:
        time = datetime.datetime.now()
        f.write(f'[log] {time} - {client.user.name} - {client.user.id} \n')

@client.event
async def on_resumed():
    print("Resumed connectivity!")


extensions = [
#    'cogs.events',
    'cogs.auto',
#    'cogs.owner'
#    'cogs.cmds'
]

if __name__ == "__main__":
    for ext in extensions:
        client.load_extension(ext)

# run
client.run(os.environ['DISCORD_TOKEN'])
