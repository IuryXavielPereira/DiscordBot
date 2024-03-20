# loading .env
from dotenv import load_dotenv
load_dotenv()

# importing constans
from config.constants import DISCORD_TOKEN, LOGGING_FORMAT, DATE_FORMAT

# defining logging pattern
import logging
logging.basicConfig(format=LOGGING_FORMAT, datefmt=DATE_FORMAT)

# importing the bot client class
from classes import botClientClass
import discord

intents = discord.Intents.all()
client = botClientClass.BotClient(intents=intents)
client.run(DISCORD_TOKEN)