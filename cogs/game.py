import discord
import asyncio
import random
from random import choice
from discord.ext import commands, tasks

rd = []

class Game(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        self.clear_rd.start()

    @tasks.loop(minutes=1.0)
    async def clear_rd(self):
        rd.clear()
    
    @clear_rd.before_loop
    async def before_printer(self):
        await self.client.wait_until_ready()

    @commands.command(aliases=['best', '_rand'])
    async def tag(self, ctx):
        user = choice(ctx.channel.guild.members)
        context = ['best', 'worst', 'most handsome', 'coolest']
        await ctx.send(f"{user.mention} is the {choice(context)}!!")

    @commands.command(aliases=['question', 'ball'])
    async def ask(self, ctx, *, question):
        await ctx.channel.purge(limit=1)
        answers = ['It is certain', 
                   'It is decidedly so', 
                   'Without a doubt', 
                   'Yes – definitely', 
                   'You may rely on it', 
                   'As I see it, yes', 
                   'Most likely', 
                   'Outlook good', 
                   'Yes Signs point to yes', 
                   'Reply hazy', 
                   'Cannot predict now', 
                   'Concentrate and ask again', 
                   'Dont count on it', 
                   'My reply is no', 
                   'My sources say no', 
                   'Outlook not so good', 
                   'Very doubtful']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(answers)}')

    @commands.command(aliases=['rd_check', 'rdc', 'rc'])
    async def ready_check(self, ctx, member:discord.Member):
        await ctx.channel.purge(limit=1)
        if member not in rd:
            rd.append(member)
            embed=discord.Embed(title="Ready Check", description=f"{ctx.author.name} is waiting for {member.mention}!!", color=0x7a9bc7)
            embed.set_footer(text=f"Time is ticking...")
            await ctx.send(embed=embed)

    @commands.command(aliases=['rd', 'r'])
    async def ready(self, ctx):
        if ctx.author in rd:
            rd.remove(ctx.author)
            await ctx.send(f'{ctx.author.name} is ready!! :sunglasses:')

    @commands.command(aliases=['nrd', 'nr'])
    async def not_ready(self, ctx):
        if ctx.author in rd:
            rd.remove(ctx.author)
            await ctx.send(f'{ctx.author.name} is not ready!! :sob:')

    @commands.command()
    async def rd_list(self, ctx):
        await ctx.channel.purge(limit=1)
        l = ["• {0.name}".format(entry) for entry in rd]
        if not l:
            await ctx.send("None!!")
            return
        embed=discord.Embed(title="Ready Check List", description= "\n".join(l), color=0xffba42)
        embed.set_footer(text="-3-")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Game(client))
