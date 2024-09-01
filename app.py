import os
import discord
from discord.ext import commands

# 봇 인스턴스 생성
intents = discord.Intents.default()
intents.message_content = True  # 메시지 콘텐츠 인텐트 활성화

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.event
async def on_message(message):
    # 봇 자신의 메시지는 무시
    if message.author == bot.user:
        return
    
    # 사용자가 "hi"라고 입력하면 "hello"로 응답
    if message.content.lower() == 'hi':
        await message.channel.send('hello')
    
    # 다른 명령어도 처리할 수 있도록 on_message에서 명령어 처리기를 호출
    await bot.process_commands(message)

bot.run(os.getenv('DISCORD_BOT_TOKEN'))
