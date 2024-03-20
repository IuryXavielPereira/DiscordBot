import subprocess
import os
from config.constants import MUSIC_FOLDER
from utils.message import send_message

async def add_music_command(bot, message, args):
    if len(message.attachments) > 0:
        attachment = message.attachments[0]
        
        if attachment.filename.endswith('.mp3'):
            filename = attachment.filename.replace('_', ' ')
            file_path = os.path.join(MUSIC_FOLDER, filename)
            await attachment.save(file_path)
            
            subprocess.run(f'cd {MUSIC_FOLDER} && git add . && git commit -m "{attachment.filename}" && git push', shell=True)
            
            await send_message(bot, 'Música adicionada e alterações enviadas para o repositório Git.')
        else:
            await send_message(bot, 'Formato de arquivo inválido. Apenas arquivos .mp3 são permitidos.')
    else:
        await send_message(bot, 'Nenhum arquivo anexado. Por favor, anexe um arquivo .mp3 para adicionar uma música.')
