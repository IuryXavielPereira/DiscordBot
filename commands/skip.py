import logging
from utils.utils import stop_voice_client

async def skip_command(bot, message):
    await stop_voice_client(bot, message)
    logging.info("Music skipped")