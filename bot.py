# bot.py Initializes the bot and handles startup
import discord
from discord.ext import commands
from commands import register_commands
from database import init_db

# Initialize bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

if __name__ == "__main__":
    init_db()
    register_commands(bot)
    bot.run("TOKEN")
