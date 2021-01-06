import discord
from discord.ext import commands,tasks
from itertools import cycle
import discordlists
from discord.utils import get
import time

class server(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        self.api = discordlists.Client(self.client)

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot ready!!')
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=str(self.api.server_count) + ' servers | -help'))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        embed=discord.Embed(title="Welcome", description=f"You are member of {member.guild} right now!!", color=0x5dbfea)
        embed.add_field(name="Owner:", value=f"{member.guild.owner}", inline=True)
        embed.set_footer(text="Hi!")
        await member.send(embed=embed)

    @commands.command()
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount+1)

    @commands.command()
    async def d_clear(self, ctx):
        category = discord.utils.get(ctx.guild.categories)
        guild = ctx.message.guild
        name = ctx.message.channel
        await ctx.message.channel.delete()
        await guild.create_text_channel(f'{name}', category=category)

    @commands.command()
    async def kick(self, ctx, member:discord.Member, *, reason="no reason."):
        await ctx.channel.purge(limit=1)
        embed=discord.Embed(title=f"Kicked from {member.guild}", description=(f'You have been kicked by {ctx.author}'), color=0xfff942)
        embed.add_field(name='Reason', value=reason, inline=True)
        embed.set_footer(text="See ya!!")
        await member.send(embed=embed)
        await member.kick(reason=reason)

    @commands.command()
    async def ban(self, ctx, member:discord.Member, *, reason="no reason."):
        await ctx.channel.purge(limit=1)
        embed=discord.Embed(title=f'Banned from {member.guild}', description=(f'You have been banned by {ctx.author}'), color=0xff4242)
        embed.add_field(name='Reason', value=reason, inline=True)
        embed.set_footer(text='Bye!!')
        await member.send(embed=embed)
        await member.ban(reason=reason)

    @commands.command()
    async def unban(self, ctx, member):
        bans = await ctx.guild.bans()
        for ban in bans:
            if member == ban.user.name:
                embed=discord.Embed(title='Unbanned', description=(f'{ban.user} has been unbanned by {ctx.author}'), color=0x42e9ff)
                embed.set_footer(text=(f'Congrats!! {ban.user}'))
                await ctx.guild.unban(ban.user)
                await ctx.send(embed=embed)
            else:
                await ctx.send(f'{member} didn\'t get banned')

    @commands.command()
    async def banlist(self, ctx):
        await ctx.channel.purge(limit=1)
        bans = await ctx.guild.bans()
        pretty_list = ["• {0.user.name}#{0.user.discriminator} -Reason: {0.reason}".format(entry) for entry in bans]
        if not pretty_list:
            await ctx.send("No one get banned!!")
            return
        embed=discord.Embed(title="Banlist", description= "\n".join(pretty_list), color=0xffba42)
        embed.set_footer(text="-3-")
        await ctx.send(embed=embed)

    @commands.command()
    async def invite(self, ctx):
        link = await ctx.channel.create_invite(max_use=1,unique=True)
        embed=discord.Embed(title="Invitation", description=f"link for join {ctx.guild} server.\n{link}", color=0xc8a3ff)
        embed.add_field(name="Owner:", value=f"{ctx.guild.owner}", inline=True)
        embed.set_footer(text="New friend!!")
        await ctx.message.author.send(embed=embed)

    @commands.command()
    async def mute(self, ctx, member:discord.Member, *, reason='no reason.'):
        await ctx.channel.purge(limit=1)
        embed=discord.Embed(title="Muted", description=f"You have been muted by {ctx.author}", color=0xff3898)
        embed.add_field(name="Reason", value=f"{reason}", inline=True)
        embed.set_footer(text="Shhhh....")
        await member.send(embed=embed)
        await member.edit(mute=True)
    
    @commands.command()
    async def unmute(self, ctx, member:discord.Member):
        await ctx.channel.purge(limit=1)
        embed=discord.Embed(title="Unmuted", description=f"You have been unmuted by {ctx.author}", color=0x387eff)
        embed.set_footer(text="Talk!!")
        await member.send(embed=embed)
        await member.edit(mute=False)
    
    @commands.command()
    async def deaf(self, ctx, member:discord.Member, *, reason='no reason.'):
        await ctx.channel.purge(limit=1)
        embed=discord.Embed(title="Deaf", description=f"You have been deafened by {ctx.author}", color=0xF397D6)
        embed.add_field(name="Reason", value=f"{reason}", inline=True)
        embed.set_footer(text="....")
        await member.send(embed=embed)
        await member.edit(deafen=True)

    @commands.command()
    async def undeaf(self, ctx, member:discord.Member):
        await ctx.channel.purge(limit=1)
        embed=discord.Embed(title="Unmuted", description=f"You have been deafened by {ctx.author}", color=0xF397D6)
        embed.set_footer(text="Can ya hear?")
        await member.send(embed=embed)
        await member.edit(deafen=False)
    
    @commands.command()
    async def stfu(self, ctx, member:discord.Member):
        await ctx.channel.purge(limit=1)
        embed=discord.Embed(title="KEEP YOUR MOUTH SHUT", description=f"Your mouth has been shut by {ctx.author}", color=0xE71D36)
        embed.set_footer(text="SHUT THE F*CK UP!!")
        await member.send(embed=embed)
        await member.edit(deafen=True, mute=True)

    @commands.command()
    async def ping(self, ctx):
        await ctx.channel.purge(limit=1)
        await ctx.send(f'Pong {round(self.client.latency * 1000)}ms')
    

def setup(client):
    client.add_cog(server(client))