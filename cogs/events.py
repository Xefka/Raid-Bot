from discord.ext import commands
import discord
from datetime import date, datetime, timedelta
import datetime
import json
import asyncio
import json

logs = {}
joins = {}
timeout = 0.1

class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot:
            return
        
        if message.content == f'<@!{self.bot.user.id}>':
            print('a')
            await message.channel.send(f'**My prefix here is** `?`')
        
        elif (message.content).lower().startswith('Style'.lower()):
            name = message.content.split(" ")[1].lower()
            with open('settings/style.json', 'r') as data:
                datastore = json.load(data) #sort_keys=True
                if name in str(datastore):
                    category = await message.guild.create_category("Read Me")
                    for se in datastore['settings']:
                        datastyle = datastore[name]
                        if datastyle[se] != "":
                            payload = se + "-" + datastyle[se]
                            channel = await message.guild.create_text_channel(payload, category=category)
                            await channel.set_permissions(message.guild.default_role, send_messages=False)
                    

        elif message.content.startswith('?help'):
            pay = f'The prefix for {message.guild.name} is `?`\nYou can find a list of commands at https://www.dynobot.net/commands'
            embed = discord.Embed(
                description=f'[All Commands](https://www.dynobot.net/commands)\n[Dyno Discord](https://discordapp.com/invite/9W6EG56)\n[Add To Your Server](https://discordapp.com/oauth2/authorize?client_id={self.bot.user.id}&scope=bot&permissions=8)\n[Donate](https://dyno.gg/upgrade)',
                colour = 0x262629
            )
            embed.set_author(
                name='Additional links and help',
            )
            await message.channel.send(pay, embed=embed)

        elif message.content.startswith('?info'):
            embed = discord.Embed(colour = 0x1173D5)
            embed.set_author(name=self.bot.user.name,icon_url='https://cdn.dyno.gg/dyno-av-v3x1024.png')
            embed.add_field(name="Version",
                value='4.0.0',
                inline=True)
            embed.add_field(name='Library',
                value='eris',
                inline=True)
            embed.add_field(name='Creator',
                value='NoobLance#0002',
                inline=True)
            embed.add_field(name="Servers",
                value='160',
                inline=True)
            embed.add_field(name="Users",
                value='383238',
                inline=True)
            embed.add_field(name="Website",
                value='[dyno.gg](http://dyno.gg/)',
                inline=True)
            embed.add_field(name="Invite",
                value='[dyno.gg/invite](http://dyno.gg/invite)',
                inline=True)
            embed.add_field(name="Discord",
                value='[dyno.gg/discord](http://dyno.gg/discord)',
                inline=True)
            embed.add_field(name="Donate",
                value='[dyno.gg/donate](http://dyno.gg/donate)',
                inline=True)

            embed.set_footer(text="Alpha2 | Cluster 1 | Shard 3 | Uptime 1 day, 19 hrs, 7 mins, 10 secs",)

            await message.channel.send(embed=embed)
        
        elif message.content.startswith('?premium'):
            embed = discord.Embed(description=f"Premium is an exclusive version of {self.bot.user.name} with premium features, and improved quality / uptime.\nIt's also a great way to support {self.bot.user.name} development and hosting!",
                colour = 0xF4A00E
            )
            embed.set_author(
                name=f'{self.bot.user.name} Premium',
                icon_url='https://cdn.dyno.gg/dyno-premium-64.png'
            )
            embed.add_field(name="Features",
                value="""
                `▶` Hosted on private/dedicated servers for 99.99%  uptime.
                `▶` Volume control, playlists, Soundcloud, and more saved queues.
                `▶` Slowmode: Managing chat speed per user or channel.
                `▶` Autopurge: Purge messages at set times.
                `▶` Higher speed/performance and unnoticeable restarts or downtime.
                `▶` Fewer performance-based limits.
                """,
                inline=True
            )
            embed.add_field(name='Get Premium',
                value='You can upgrade today at https://www.dynobot.net/upgrade',
                inline=False
            )
            await message.channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
        bad = ['help','purge','clear','mode','reload', 'sad', 'support']
        if ctx.command.name in bad:
            pass
        else:
            embed = discord.Embed(
                colour = 0x03CB4E,
                description=f'Command `{ctx.command.name}` has been successfully executed.',
                timestamp=datetime.datetime.now(datetime.timezone.utc)
            )
            embed.set_author(
                name="Successfully",
                icon_url=ctx.message.author.avatar_url
            )
            embed.set_footer(
                text=str(ctx.guild.id),
                icon_url=ctx.guild.icon_url
            )
            try:
                await ctx.message.author.send(embed=embed, delete_after=120)
            except:
                pass

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if isinstance(error, commands.CommandNotFound):
            return
        elif isinstance(error, commands.CommandOnCooldown):
            try:
                await ctx.message.delete()
                await ctx.channel.send("**{}**, please cool down! ({:.0f} seconds left)".format(ctx.message.author.name,error.retry_after), delete_after=5)
            except discord.errors.Forbidden:
                await ctx.message.author.send("**{}**, please cool down! ({:.0f} seconds left)".format(ctx.message.author.name,error.retry_after), delete_after=30)

        else:
            try:
                await ctx.message.delete()
            except:
                pass
            embed = discord.Embed(
                description=str(error),
                colour = discord.Colour.dark_purple(),
                timestamp=datetime.datetime.now(datetime.timezone.utc)
            )
            embed.set_author(
                name=f"/{ctx.command.qualified_name}",
                icon_url=ctx.author.avatar_url
            )
            embed.set_footer(
                text=str(ctx.guild.name),
                icon_url=ctx.guild.icon_url
            )
            try:
                await ctx.message.author.send(embed=embed, delete_after=180)
            except:
                pass

def setup(bot):
    bot.add_cog(events(bot))