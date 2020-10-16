#bot.py
import os, discord, schedule, time, datetime
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
timeTuple = ("day", "hour", "minute", "second")

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Ready")
    async def alert():
        for guild in bot.guilds:
            print(guild)
            for channel in guild.text_channels:
                if(channel.name == "general"):
                    await channel.send("It's Tuesday Bitches! The Tuesday clock has been reset.")

    schedule.every().tuesday.do(alert)

@bot.command(name='update', help='Provides the current status of the tuesday clock')
async def update(ctx):
    msg = "I am Idris Elba, "

    now = datetime.datetime.utcnow() - datetime.timedelta(hours=7)

    if(now.weekday() == 2):
        msg += "and it's Tuesday today! There are "
    else:
        msg += "and there are "

    days = (7 - now.weekday()) % 7

    midnight = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(days=1)
    delta = midnight - now

    times = [days, delta.seconds//3600, (delta.seconds//60)%60, delta.seconds%60]

    for time, name in zip(times, timeTuple):
        msg += str(time) + " " + str(name) + (" " if days == 1 else "s ")

    msg += "until Tuesday."

    await ctx.send(msg)

bot.run(TOKEN)