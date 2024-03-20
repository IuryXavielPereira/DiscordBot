import os

# creating discord constants
DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
TARGET_CHANNEL = int(os.environ["TARGET_CHANNEL"])
COMMANDS_PREFIX = os.environ["COMMANDS_PREFIX"]
MUSIC_VOLUME = 1

# folders path
MUSIC_FOLDER = os.environ["MUSIC_FOLDER"]
PLAYLIST_FOLDER = os.environ["PLAYLIST_FOLDER"]

# logging
LOGGING_FORMAT='%(asctime)s - %(message)s'
DATE_FORMAT='%Y-%d-%b- %H:%M:%S'