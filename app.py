import os
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, world!")

bot.run(os.getenv('DISCORD_BOT_TOKEN'))
