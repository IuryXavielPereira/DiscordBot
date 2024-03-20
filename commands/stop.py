import logging
from utils.message import send_message
from utils.utils import stop_voice_client

async def stop_command(bot, message):
    await bot.clear_queue()
    await stop_voice_client(bot, message)
    await send_message(bot, "Musica Parada")
    logging.info("Music Stopped")
