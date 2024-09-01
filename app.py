import os
import discord
from discord.ext import commands
import requests

# 봇 인스턴스 생성
intents = discord.Intents.default()
intents.message_content = True  # 메시지 콘텐츠 인텐트 활성화

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command(name='add')
async def add(ctx, *, content: str):
    # Google Forms의 제출 URL
    url = 'https://docs.google.com/forms/d/e/1FAIpQLSfmTGJHQGjepy09H1jmc4svhJaYlaBdbbzU800dcjzOEScb-w/formResponse'
    
    # Google Forms의 각 필드에 해당하는 entry 번호를 설정
    form_data = {
        'entry.972880290': content,  # 사용자가 입력한 내용
    }
    
    # POST 요청을 통해 폼 제출
    response = requests.post(url, data=form_data)
    
    # 요청 결과에 따라 메시지를 보내기
    if response.status_code == 200:
        await ctx.send(f'내용이 성공적으로 제출되었습니다: {content}')
    else:
        await ctx.send(f'제출 실패: {response.status_code}')

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

# 환경 변수에서 Discord Bot Token 가져오기
bot.run(os.getenv('DISCORD_BOT_TOKEN'))
