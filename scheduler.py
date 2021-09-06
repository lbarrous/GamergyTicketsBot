import os

import schedule
from dotenv import load_dotenv

from gamergyBot import bot

load_dotenv()

# bot and chat ids
botID = os.getenv('BOT_ID')
chatID = os.getenv('CHAT_ID')

# schedule crawler
schedule.every(10).minutes.do(bot(botID, chatID))

# run script infinitely
while True:
    schedule.run_pending()
