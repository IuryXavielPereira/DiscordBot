import logging
from config.constants import MUSIC_FOLDER
from utils.message import send_message
from utils.utils import join_path, get_all_by_path, order_and_join

async def play_command(bot, message, song_name):
    musics = get_all_by_path(MUSIC_FOLDER, song_name)
    if len(musics) == 1:
        audio_file = join_path(MUSIC_FOLDER, musics[0])
        voice_channel = message.author.voice.channel

        if len(bot.get_music_queue()) == 0:
            await bot.add_music_to_queue(audio_file)
            await bot.play_music(voice_channel)
            logging.info(f"Playing music: {musics[0]}")
        else:
            await bot.add_music_to_queue(audio_file)
            await send_message(bot, f"Musica adicionada a fila: {musics[0]}")
            logging.info(f"Added music to queue: {musics[0]}")

    elif len(musics) > 1:
        message = order_and_join(musics)
        await send_message(bot, f"Escolha uma musica:\n{message}")
        logging.info("2 or more found musics")
    else:
        await send_message(bot, f"Nenhuma musica com o nome: {song_name}")
        logging.info(f"Music unavailable: {song_name}")