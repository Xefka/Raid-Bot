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

client.remove_command("help")

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
    'cogs.events',
    'cogs.auto',
    'cogs.owner',
    'cogs.cmds'
]

files = [
    'settings/login.json',
    'settings/style.json',
    'logs/log.txt'
]
if __name__ == "__main__":
    for ext in extensions:
        client.load_extension(ext)
# check files
for file in files:
    if os.path.isfile(file) == False:
        if "/" in file:
            fdir = file.split("/")
            for d in fdir:
                if "." in d:
                    break
                os.mkdir(fdir[0])
            
        fh = open (file, "w")
        fh.write("{}")
        fh.close()
        print(f"[+] File {file} has been Successfully Created.")

with open('settings/login.json', 'r') as login:
    datastore = json.load(login)
    if datastore['environ'] == True:
        token = datastore['environ']
    if datastore['token'] != False:
        token = datastore['token']
    # is bot
    isbot = datastore['bot']

# run
client.run(token, bot=isbot)