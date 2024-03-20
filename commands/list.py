import logging
import os
from config.constants import MUSIC_FOLDER
from utils.message import send_message
from utils.utils import order_and_join, get_all_name

async def list_command(bot, message, args):
        musics=[]
        if args:
                musics = get_all_musics_filter(MUSIC_FOLDER, args)
        else:
                musics = get_all_name(MUSIC_FOLDER)

        musics_message = order_and_join(musics)

        if musics_message:
                truncated_message = truncate_message(musics_message, 2000)
                for chunk in truncated_message:
                        await send_message(bot, chunk)
        else:
                await send_message(bot, "Nenhuma música encontrada")
        logging.info("Listing musics")

def get_all_musics_filter(path, name):
        matching = []
        for file in os.listdir(path):
                if name.lower() in file.lower():
                        matching.append(file[0:-4])
        return matching

def truncate_message(message, limit):
    if len(message) <= limit:
        return [message]

    chunks = []
    current_chunk = ""
    songs = message.split('\n')

    for song in songs:
        if len(current_chunk) + len(song) + 1 >= limit:
                chunks.append(current_chunk)
                current_chunk = "" 
        else:
            current_chunk += song + '\n'

    if current_chunk:
        chunks.append(current_chunk)

    return chunks