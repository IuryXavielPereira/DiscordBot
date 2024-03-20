import logging
from commands.play import play_command
from commands.playlist import playlist_command
from commands.stop import stop_command
from commands.skip import skip_command
from commands.list import list_command
from commands.create_playlist import create_playlist
from commands.queue import queue_command
from commands.add_music import add_music_command

from utils.message import send_message

async def process_command(bot, message):
        command_parts = message.content.split(" ", 1)
        command = command_parts[0][1:]
        args = command_parts[1] if len(command_parts) > 1 else None

        possible_commands = {
            "play":             lambda: play_command(bot, message, args),
            "playlist":         lambda: playlist_command(bot, message, args),
            "stop":             lambda: stop_command(bot, message),
            "skip":             lambda: skip_command(bot, message),
            "list":             lambda: list_command(bot, message, args),
            "create_playlist":  lambda: create_playlist(bot, message, args),
            "add_music":        lambda: add_music_command(bot, message, args),
            "queue":        lambda: queue_command(bot),
        }
        
        cmd = possible_commands.get(command)
        if cmd:
            await cmd()
        else:
            await send_message(bot, f"Comando inválido: {command}")

        logging.warning(f"Command: {command}, Arguments: {args}")