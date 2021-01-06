import discord
from discord.ext import commands
from datetime import date
from random import randint

class Help(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        client.remove_command('help')

    @commands.command()
    async def help(self, ctx):

        colors = randint(0, 0xffffff)

        embed=discord.Embed(title="-MOON- Help", description="All current visible commands!!", color=colors)
        embed.add_field(name="-ping", value="Display server's ping\n⠀", inline=True)
        embed.add_field(name="-clear (n)", value="Clear messages", inline=True)
        embed.add_field(name="-d_clear", value="Clear current text ch.", inline=True)

        embed.add_field(name="-kick (@name)", value="Kick mentioned member\n⠀", inline=True)
        embed.add_field(name="-ban (@name)", value="Ban mentioned member", inline=True)
        embed.add_field(name="-unban (name)", value="Unban (name)", inline=True)

        embed.add_field(name="-banlist", value="List all banned member\n⠀", inline=True)
        embed.add_field(name="-invite", value="Create invite link", inline=True)
        embed.add_field(name="-mute (@name)", value="Mute mentioned member", inline=True)

        embed.add_field(name="-unmute (@name)", value="Unmute mentioned member\n⠀", inline=True)
        embed.add_field(name="-ask (question)", value="8ball answer", inline=True)
        embed.add_field(name="-tag", value="Randomness :D", inline=True)

        embed.add_field(name="-rdc (@name)", value="Ready check!!)\n⠀", inline=True)
        embed.add_field(name="-stfu (@name)", value="SHUT THE F*CK UP!! :face_with_symbols_over_mouth: \n⠀", inline=True)
        embed.add_field(name="-deaf (@name)", value="Deaf mentioned member", inline=True)

        embed.add_field(name="-undeaf (@name)", value="Undeaf mentioned member\n⠀", inline=True)
        embed.add_field(name="-bed (@name)", value="Sleep~~ :sleeping:", inline=True)

        embed.add_field(name="-whisper (@name) (text)", value="Send private dm to mentioned member\n⠀", inline=False)
        embed.add_field(name=":clock7: Incoming command(s)", value="No ideas :cry:", inline=True)
        embed.set_footer(text=date.today())

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Help(client))