import discord
import asyncio
from discord import FFmpegPCMAudio, PCMVolumeTransformer
import logging

from config.constants import TARGET_CHANNEL, COMMANDS_PREFIX, MUSIC_VOLUME
from commands.commands import process_command
from utils.message import send_message


class BotClient(discord.Client):
    async def on_ready(self):
        logging.info("Logged on as {0}!".format(self.user))
        await send_message(self, f"Tocando agora: {self.music_queue[0][9:-4]}")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.music_queue = []

    async def on_message(self, message):
        if message.author.bot:
            logging.info("Message from bot")
            return
        
        if message.content.startswith(COMMANDS_PREFIX) and message.channel.id == TARGET_CHANNEL:
            logging.warning("Message from {0.author}: {0.content}".format(message))
            await process_command(self, message)

    # music_queue
    async def add_music_to_queue(self, audio_file):
        self.music_queue.append(audio_file)

    def get_music_queue(self):
        return self.music_queue

    async def clear_queue(self):
        self.music_queue = []

    async def pop_first_music_from_queue(self):
        self.music_queue.pop(0)

    #voice client
    async def get_voice_client(self, voice_channel):
        voice_client = voice_channel.guild.voice_client

        if voice_client and voice_client.is_connected():
            vc = voice_client
        else:
            vc = await voice_channel.connect()

        if not vc.is_connected():
            await vc.connect()

        return vc
    
    # music player
    async def handle_after(self, voice_channel, error):
        print(error)
        if not error:
            await self.pop_first_music_from_queue()
            await self.play_music(voice_channel)
        else:
            await self.play_music(voice_channel)

    async def play_music(self, voice_channel):
        vc = await self.get_voice_client(voice_channel)

        if len(self.music_queue) > 0:
            logging.warning(f"Queue: {self.music_queue}")
            await send_message(self, f"Tocando agora: {self.music_queue[0][9:-4]}")

            audio_source = discord.FFmpegPCMAudio(self.music_queue[0])
            volume = discord.PCMVolumeTransformer(audio_source, volume=MUSIC_VOLUME)

            vc.play(
                volume,
                after=lambda error: asyncio.run_coroutine_threadsafe(
                    self.handle_after(voice_channel, error), self.loop
                ),
            )

        else:
            asyncio.run_coroutine_threadsafe(vc.disconnect(), self.loop)
