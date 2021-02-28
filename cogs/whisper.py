import discord
from discord.ext import commands
from random import choice, randint, random


class Whisper(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=['w', 'secret', 'text'])
    async def whisper(self, ctx, member: discord.Member, *, message=''):
        if message == '':
            msg = ['hi', 'hello']
            message = choice(msg)
        await member.send(message)
        await ctx.channel.purge(limit=1)

    @commands.command(aliases=['bye', 'bed'])
    async def goodnight(self, ctx, member: discord.Member):
        await ctx.channel.purge(limit=1)
        message = [
            'Enjoy your adventure in the forest of dreams.',
            'Good night and sleep tight!',
            'Wishing you the sweetest dreams as you drift off to sleep.',
            'May your dreams be kind tonight.',
            'As the day turns into night, keep your worries out of sight.',
            'Let the fairies make your sleep wonderful. Good night.',
            'No matter how bad the day was, always try to end it with positive thoughts. Try to focus on the next day and hope for a sweet dream. Good night.',
            'May all the worries disappear from your life. Good Night!',
            'Sweet dream!!',
            'Night night!!',
        ]
        colors = randint(0, 0xffffff)
        embed = discord.Embed(
            title=f"from {ctx.author.name}", description=f"{choice(message)}", color=colors)
        embed.set_footer(text="Hope you dream of me ~")
        await member.send(embed=embed)


def setup(client):
    client.add_cog(Whisper(client))
