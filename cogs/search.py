import os
import discord

from dotenv import load_dotenv
from discord.ext import commands
from googleapiclient.discovery import build

load_dotenv()
api_key = os.getenv('GOOGLE_API')
cse_key = os.getenv('CSE_ID')

def google_search(search_term, api_key, cse_id, **kwargs):
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
        return res

class Search(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["wiki_search", "w_search", "search"])
    async def wikisearch(self, ctx, *, message):
        start_res = google_search(message , api_key, cse_key)

        result = start_res["items"][0]
        snippet = result["snippet"]
        snippet = snippet.replace('\n',' ')
        text = snippet + "\n\n :face_with_monocle:   Continue reading at : " + result["link"] + "\n⠀"
        embed=discord.Embed(title=result["title"], description=text, color=0x85ffda)
        
        result = result["pagemap"]
        start_res = start_res["items"]
        if len(start_res) > 1:
            txt = start_res[1]["link"]
            embed.add_field(name="Other search result : ", value=f"⠀⠀• {txt}", inline=False)
        if "cse_image" in result:
            embed.set_image(url = result["cse_image"][0]["src"])
        
        embed.set_footer(text="*wink*")
        await ctx.send(embed=embed)
    
def setup(client):
    client.add_cog(Search(client))