import os
import discord
from discord.ext import commands

# 필요한 권한을 설정
intents = discord.Intents.default()
intents.message_content = True  # 메시지 콘텐츠를 읽는 권한을 설정

# 봇 객체를 생성할 때 intents를 추가
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, world!")

bot.run(os.getenv('DISCORD_BOT_TOKEN'))
