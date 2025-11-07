from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID", "9043884")
APP_HASH = os.environ.get("APP_HASH", "733596982db7e73247489b26b1a55662")
SESSION = os.environ.get("SESSION","جلسة تليثون")
fraon = TelegramClient(StringSession(SESSION), APP_ID, APP_HASH)
fraon.start()
