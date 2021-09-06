import os
from pprint import pprint

import telepot
from dotenv import load_dotenv

from ticketsAvailabilityScrapper import getTicketsAvailability

load_dotenv()


def bot():

    # bot and chat ids
    botID = os.getenv('BOT_ID')
    chatID = os.getenv('CHAT_ID')

    pprint(botID)
    pprint(chatID)

    bot = telepot.Bot(botID)
    ticketsAvailability = getTicketsAvailability()

    if ticketsAvailability == True:
        bot.sendMessage(chatID, 'Tickets available!')
    else:
        bot.sendMessage(chatID, 'Tickets NOT available!')
