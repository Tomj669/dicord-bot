import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
        if 'kirat bhaiya' in message.content.lower() or 'kirat sir' in message.content.lower():
        await message.author.send("Dude just STOP!")

    await bot.process_commands(message)

bot.run('MTExNTY1NTI3MDkxNjQyNzgwNw.GwDlVK.4YFaVHRD5u-S6b1QFLi7H9XC6_oldelfcaGJ34')
