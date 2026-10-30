import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import asyncio
from discord import app_commands

# Load the bot
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
print(discord.__version__)
# Setup Logging
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
logging.basicConfig(level=logging.DEBUG, handlers=[handler])

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Prefix and Application ID for slash command
bot = commands.Bot(command_prefix='!', intents=intents, application_id=1563539727288762490)

# Activity and Sync
@bot.event
async def on_ready():
    activity = discord.Game(name="Saki Renewed | discord.gg/vietrhythm")
    await bot.change_presence(activity=activity)

    print(f"{bot.user.name} đã được khởi động!")
    try:
        synced = await bot.tree.sync()
        print(f"Đã đồng bộ hóa {len(synced)} lệnh.")
    except Exception as e:
        print(f"Error syncing commands: {e}")

# Rena gay
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.strip().lower() == "rena":
        await message.channel.send("gay\ngay\ngay\ngay")
    if message.content.strip().lower() == "cot":
        await message.channel.send("gay\ngay\ngay\ngay")
    if message.content.strip().lower() == "christmas":
        await message.channel.send("rich")
    if message.content.strip().lower() == "xèo xèo":
        await message.channel.send("https://i.ibb.co/jkQB4WXP/IMG-20260814-190551.jpg")
    if message.content.strip().lower() == "cá rán":
        await message.channel.send("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQcrYH9seUHlSbhLhaS5GgC2egCbIh61oKJVS2V67sp3A&s=10")
    if message.content.strip().lower() == "đạt đùi nuột":
        await message.channel.send("https://i.ibb.co/1qcmHfX/rn-image-picker-lib-temp-8accd7b7-9ded-42d6-a983-107287d19ce1.jpg")
    await bot.process_commands(message)

# Load Cogs
async def main():
    await bot.load_extension('cogs.ping')
    await bot.load_extension('cogs.welcome')
    await bot.load_extension('cogs.afk')
    await bot.load_extension('cogs.leveling')
    await bot.load_extension('cogs.economy')
    await bot.load_extension('cogs.cookie')
    await bot.load_extension('cogs.daily_message')
    await bot.load_extension('cogs.omikuji')
    await bot.load_extension('cogs.editmessage')
    await bot.start(token)

if __name__ == "__main__":
    asyncio.run(main())
