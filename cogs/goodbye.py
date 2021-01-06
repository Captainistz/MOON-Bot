#27-10-62 | Pumpui
import discord
from discord.ext import commands
from datetime import date

class GoodBye(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def goodbye(self, ctx):
        d = date.today() - date(2020, 8, 5)
        await ctx.send(f"for {d.days} days")
    #Thanks for everything, I'll never forget :D Goodluck (283 days)

def setup(client):
    client.add_cog(GoodBye(client))
