import discord
from discord.ext import commands

word = {
    "Hello": "wèi",
    "Thanks": "xiè xiè",
    "Very good": "hĕn piàoliang",
    "I don't know": "wǒ bù dǒng",
    "Sorry": "duì bù qǐ",
    "Go": "zǒu",
    "Come": "lái",
    "Don't": "bù yào",
    "Wait": "děng",
    "Wait": "děng",
    "Wait": "děng",
    "Wait": "děng",
    "Wait": "děng",
    "Wait": "děng",
    "Wait": "děng",
    "Wait": "děng",
    "Wait": "děng"
}
word = list(word.items())
print(word[9:18])

class Chinese(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['chinese', 'china'])
    async def pinyin(self, ctx, *, message='1'):
        if message.isnumeric():
            cur = int(message)
            embed = discord.Embed(title="Chinese", color=0xff3333)
            for key, val in word[(cur-1)*9:cur+cur*9]:
                embed.add_field(name=key, value=val, inline=True)
            await ctx.channel.purge(limit=1)
            await ctx.send(embed=embed)
        else:
            await ctx.send(message)


def setup(client):
    client.add_cog(Chinese(client))
