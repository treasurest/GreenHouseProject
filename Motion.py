import RPi.GPIO as GPIO
import discord
import asyncio
from discord.ext import commands
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO_PIR = 4 #pin 7
GPIO_LED = 27 # pin 13

GPIO.setup(GPIO_LED, GPIO.OUT)
GPIO.setup(GPIO_PIR, GPIO.IN)

TOKEN = 'ODUxODc0MjEyNDk0NTczNjA5.YL-nrw.EMcT1FQAqgernlu5F0zs3cNbVD0'
STATUS_UPDATE_CHANNEL_NAME = 'general'

bot = commands.Bot(command_prefix="!")

def detect_motion():
        while GPIO.input(GPIO_PIR) ==1:
            Motion = 0

        Motion = 0

        while True:
            if GPIO.input(GPIO_PIR) ==1:
                if Motion == 0:
                    print ("Motion Detected!")
                    Motion = 1


                    GPIO.output(GPIO_LED, True)
                    return True
            else:
                if Motion == 1:
                    Motion = 0
                GPIO.output(GPIO_LED, False)

        return True
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    message = f'Test Message. Attemting to detect motion'

    for guild in bot.guilds:
        for chan in guild.channels:
            if chan.name == STATUS_UPDATE_CHANNEL_NAME:
                channel = chan
                await chan.send(message)

    while True:
        motion = detect_motion()
        if motion:
            await channel.send("Motion Detected!")

bot.run(TOKEN)