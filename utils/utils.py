import os
from utils.message import send_message

def get_all_name(path):
        filenames = []
        for file in os.listdir(path):
                file_path = os.path.join(path, file)
                if os.path.isfile(file_path) and file.endswith('.mp3') or file.endswith('.txt'):
                        filenames.append(file[0:-4])
        return filenames

def get_all_by_path(path, name):
    matching = []
    for file in os.listdir(path):
        if name.lower() in file.lower():
            matching.append(file)
    return matching

def join_path(path, name):
        return os.path.join(path, name)

def order_and_join(itens):
        itens.sort()
        message = "\n".join(itens)
        return message

def get_voice_client(message):
    return message.guild.voice_client

async def stop_voice_client(bot, message):
    voice_client = get_voice_client(message)
    if voice_client and voice_client.is_playing():
        voice_client.stop()
    else:
        await send_message(bot, "Nenhuma musica tocando")