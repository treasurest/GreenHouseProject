import discord
import asyncio
from discord.ext import commands
from gpiozero import LightSensor
import time


LDR = LightSensor(17)


TOKEN = 'ODUxODc0MjEyNDk0NTczNjA5.YL-nrw.EMcT1FQAqgernlu5F0zs3cNbVD0'
STATUS_UPDATE_CHANNEL_NAME = 'general'

bot = commands.Bot(command_prefix="!")

def detect_light():
    while True:

        print(LDR.value * 1000)
        time.sleep(5)

        return LDR.value

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    message = f'Test Message. Attemting to detect light'

    for guild in bot.guilds:
        for chan in guild.channels:
            if chan.name == STATUS_UPDATE_CHANNEL_NAME:
                channel = chan
                await chan.send(message)

    while True:
        light = detect_light()
        if light:
            await channel.send(light * 1000)

bot.run(TOKEN)