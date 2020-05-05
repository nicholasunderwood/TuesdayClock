#bot.py
import os, discord, schedule, time, datetime
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

def job():
    bot.guild

s = schedule.every().wednesday.do(job)

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
    now = datetime.datetime.now()
    delta = datetime.timedelta(seconds=-now.second, minutes=-now.minute, hours=-now.hour, days=-now.weekday() + 1, weeks=1)
    days, hours, minutes, seconds = delta.days, delta.seconds//3600, (delta.seconds//60)%60, delta.seconds%60

    await ctx.send(
        "I am Idris Elba, and there are "
        f'{days} day{"" if days == 1 else "s"}, ' +
        f'{hours} hour{"" if hours == 1 else "s"}, ' +
        f'{minutes} minute{"" if minutes == 1 else "s"}, and '+
        f'{seconds} second{"" if seconds == 1 else "s"} until Tuesday.'
    )

bot.run(TOKEN)