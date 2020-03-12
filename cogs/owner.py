
from discord.ext import commands
import discord
import os
import aiohttp
import sys
import asyncio
import datetime

class owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='activity', hidden=True)
    @commands.is_owner()
    async def activity(self, ctx, type: str, *, name: str):
        type = type.lower()
        if type == 'playing':
            activity_type = discord.ActivityType.playing
        elif type == 'watching':
            activity_type = discord.ActivityType.watching
        elif type == 'listening':
            activity_type = discord.ActivityType.listening
        elif type == 'streaming':
            activity_type = discord.ActivityType.streaming

        guild_count = len(self.bot.guilds)
        member_count = len(list(self.bot.get_all_members()))
        name = name.format(guilds=guild_count, members=member_count)

        # Setting bot activity
        await self.bot.change_presence(activity=discord.Activity(type=activity_type, name=name))
        await ctx.send(f'**`Success:`** bot activity has been changed')

    @commands.command(name='status', hidden=True)
    @commands.is_owner()
    async def status(self, ctx, status: str):
        # Check which status was specified
        status = status.lower()
        if status in ['offline', 'off', 'invisible', 'ghost']:
            bot_status = discord.Status.invisible
        elif status in ['idle', 'waiting']:
            bot_status = discord.Status.idle
        elif status in ['dnd', 'disturb', 'away']:
            bot_status = discord.Status.dnd
        else:
            bot_status = discord.Status.online

        # Setting bot status
        try:
            await self.bot.change_presence(status=bot_status)
        except Exception as e:
            # Handle errors if any
            await ctx.send(f'**`ERROR:`** { type(e).__name__ } - { e }')
        else:
            await ctx.send(f'**`SUCCESS:`** bot status changed to { bot_status }')

    @commands.command(name='rename', hidden=True)
    @commands.is_owner()
    async def rename(self, ctx, *, name):
        await self.bot.user.edit(username=name)

    @commands.command(name='avatar', hidden=True)
    @commands.is_owner()
    async def avatar(self, ctx, url: str = None):
        
        if url is None:
            try:
                url = ctx.message.attachments[0]
            except IndexError:
                return await ctx.send('You did not give me any image whatsoever.')

        async with aiohttp.ClientSession() as session:
            r = await session.get(url=url)
            data = await r.read()
            await self.bot.user.edit(avatar=data)
            r.close()
        await ctx.send('Changed Avatar!')

    """ Restart Bot """
    @commands.command(name="logout", description="Kills bot instantly", aliases=['kill'])
    @commands.is_owner()
    async def logout(self, ctx):
        await ctx.send('**`Rebooting...`**')
        await self.bot.logout()
        sys.exit(6)

    @commands.command(name='reload', aliases=['restart'], hidden=True)
    @commands.is_owner()
    async def reload(self, ctx, module : str = None):
        """Reloads a cogs."""
        if module == None:
            for f in os.listdir("cogs"):
                if f.endswith('.py'):
                    cog = f.replace('.py', '')
                    if not cog.startswith("__"):
                        self.bot.reload_extension(f"cogs.{cog}")
            await ctx.send('**:white_check_mark: Cogs loaded Successfully**.')
        else:
            self.bot.reload_extension(f"cogs.{module}")
            await ctx.send(f'**:white_check_mark: Cog {module} loaded Successfully**.')

    @commands.command(name='load', aliases=['newcog'], hidden=True)
    @commands.is_owner()
    async def load(self, ctx, extension):
        self.bot.load_extension(f"cogs.{extension}")

    @commands.command(name='unload', aliases=['revcog'], hidden=True)
    @commands.is_owner()
    async def unload(self, ctx, extension):
        self.bot.unload_extension(f"cogs.{extension}")

    @commands.command(name='mail-all', hidden=True)
    @commands.is_owner()
    async def mailall(self, ctx, *, text):
        success = 0
        for member in self.bot.get_all_members:
            if success <= 3600:
                if not member.bot:
                    try:
                        text = text.format(user=member.mention, guild=ctx.guild.name)
                        await member.send(text)
                        await asyncio.sleep(1)
                        success += 1
                    except:
                        await asyncio.sleep(5)

def setup(bot):
    bot.add_cog(owner(bot))
