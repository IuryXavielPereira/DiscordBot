from config.constants import PLAYLIST_FOLDER, MUSIC_FOLDER
from utils.message import send_message
from utils.utils import join_path, get_all_by_path, order_and_join, get_all_name

async def playlist_command(bot, message, playlist_name):
        
        if not playlist_name:
             names = get_all_name(PLAYLIST_FOLDER)
             message = order_and_join(names)
             await send_message(bot, message)

        else:
            playlist = get_all_by_path(PLAYLIST_FOLDER, playlist_name)

            if len(playlist) == 1:
                playlist_file = join_path(PLAYLIST_FOLDER, playlist[0])
                voice_channel = message.author.voice.channel

                with open(playlist_file, "r") as f:
                    words_list = f.read().splitlines()
                    first_audio_file = join_path(MUSIC_FOLDER, words_list[0])
                    await bot.add_music_to_queue(first_audio_file)
                    await bot.play_music(voice_channel)

                    for music_name in words_list[1:]:
                        if music_name.endswith('.mp3'):
                            music_file = join_path(MUSIC_FOLDER, music_name)
                        else:
                            music_file = join_path(MUSIC_FOLDER, music_name+'.mp3')
                        await bot.add_music_to_queue(music_file)

            elif len(playlist) > 1:
                message = order_and_join(playlist)
                await send_message(bot,f"Escolha uma playlist:\n{message}")
            else:
                await send_message(bot,f"Nenhuma playlist com o nome: {playlist_name}")
