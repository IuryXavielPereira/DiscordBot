import logging
from utils.message import send_message
from utils.utils import order_and_join

async def queue_command(bot):
    songs_list = bot.get_music_queue()
    songs = []
    for song_path in songs_list:
        songs.append(song_path[9:-4])

    joined_message = "\n".join(songs)

    if joined_message:
        await send_message(bot, joined_message)
        logging.info('Listing Queue')
    else:
        await send_message(bot, "Queue vazia!")
        logging.warning('Empty Queue')