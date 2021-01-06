import discord
import os
import json
from discord.ext import commands
from dotenv import load_dotenv


class Levels(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_message(self, message):
        with open("cogs/user.json") as f:
            users = json.loads(f.read())
        bot_name = os.getenv('BOT_NAME')
        if message.author.name != bot_name:
            await update_data(self, users, message.author)
            await add_exp(self, users, message.author)

        with open("cogs/user.json", "w") as f:
            json.dump(users, f, indent=4, sort_keys=True)

    @commands.command()
    async def mylvl(self, ctx):
        with open("cogs/user.json") as f:
            users = json.loads(f.read())
        await ctx.send(f'{ctx.author.name} total text is : {users[str(ctx.author.id)]["text"]}')

async def update_data(self, users, user):
    if not str(user.id) in users:
        users[str(user.id)] = {}
        users[str(user.id)]["name"] = user.name
        users[str(user.id)]["text"] = 0
    
async def add_exp(self, users, user):
    users[str(user.id)]["text"] += 1

def setup(client):
    client.add_cog(Levels(client))