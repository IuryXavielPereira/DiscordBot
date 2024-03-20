import logging
from config.constants import TARGET_CHANNEL

async def send_message(bot, message):
        channel = bot.get_channel(TARGET_CHANNEL)
        await channel.send(message)
        logging.warning('Message sent')