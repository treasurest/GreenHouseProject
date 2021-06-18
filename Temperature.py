import RPi.GPIO as GPIO
import discord
import asyncio
from discord.ext import commands
from pigpio_dht import DHT11
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO_TEMP = 18 # pin 12

TEMP_SENSOR = DHT11(GPIO_TEMP)

TOKEN = 'ODUxODc0MjEyNDk0NTczNjA5.YL-nrw.EMcT1FQAqgernlu5F0zs3cNbVD0'
STATUS_UPDATE_CHANNEL_NAME = 'general'

bot = commands.Bot(command_prefix="!")

def detect_temp():
    while True:
        results = TEMP_SENSOR.read()
        print(results)
        time.sleep(5)
        return results

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    message = f'Test Message. Attemting to detect temperature'

    for guild in bot.guilds:
       for chan in guild.channels:
            if chan.name == STATUS_UPDATE_CHANNEL_NAME:
                channel = chan
                await chan.send(message)

    while True:
        temp = detect_temp()
        if temp:
            await channel.send(temp)

bot.run(TOKEN)