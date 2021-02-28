import discord
import math
import os
from discord import voice_client
from discord import client
from discord.ext import commands
from gtts import gTTS
from googletrans import Translator

words = {
    "Hello": "wèi",
    "Thanks": "xiè xiè",
    "Good": "piàoliang",
    "I don't understand": "wǒ bù dǒng",
    "Sorry": "duì bù qǐ",
    "Go": "zǒu",
    "Come": "lái",
    "Don't": "bù yào",
    "Wait": "děng",
    "Welcome": "huān yíng",
    "Good night": "wǎn ān",
    "Nice to meet u": "xìng huì",
    "I miss u": "wǒ xiǎng nǐ"
}

chinesewords = {
    "Hello": "喂",
    "Thanks": "謝謝",
    "Good": "漂亮",
    "I don't understand": "我不懂",
    "Sorry": "對不起",
    "Go": "走",
    "Come": "来",
    "Don't": "不要",
    "Wait": "等",
    "Welcome": "欢迎",
    "Good night": "晚安",
    "Nice to meet u": "幸會",
    "I miss u": "我想你"
}
word = list(words.items())
translator = Translator()


class Chinese(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['chinese', 'china'])
    async def pinyin(self, ctx, *, message='1'):
        if message.isnumeric():
            cur = int(message)
            if (cur-1)*9 >= len(word):
                cur = math.ceil((len(word)/9))
            embed = discord.Embed(title="Chinese", color=0xff3333)
            for key, val in word[(cur-1)*9:(cur*10-1) if (cur*10-1) < len(word) else len(word)]:
                embed.add_field(name=key, value=val, inline=True)
            embed.set_footer(text=f"{cur}/{(math.ceil((len(word)/9)))}")
            await ctx.channel.purge(limit=1)
            await ctx.send(embed=embed)
        else:
            if ctx.author.voice is None or ctx.author.voice.channel is None:
                return
            voice_channel = ctx.author.voice.channel
            if ctx.voice_client is None:
                vc = await voice_channel.connect()
            else:
                await ctx.voice_client.move_to(voice_channel)
                vc = ctx.voice_client
            if os.path.exists('./tmp.mp3'):
                os.remove('./tmp.mp3')
            if message in chinesewords.keys():
                finalword = chinesewords[message]
                await ctx.send(message + ' : ' + words[message])
            else:
                finalword = translator.translate(
                    message, dest='zh-CN')
                await ctx.send(finalword.origin + ' : ' + finalword.pronunciation)
                finalword = finalword.text

            tts = gTTS(text=finalword, lang='zh')
            tts.save('./tmp.mp3')
            vc.play(discord.FFmpegPCMAudio('./tmp.mp3'))

    @commands.command(aliases=['dis', 'quit'])
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()


def setup(client):
    client.add_cog(Chinese(client))
