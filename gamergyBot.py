from pprint import pprint

import telepot

from ticketsAvailabilityScrapper import getTicketsAvailability


def bot(botID, chatID):
    bot = telepot.Bot(botID)
    ticketsAvailability = getTicketsAvailability()

    if ticketsAvailability == True:
        bot.sendMessage(chatID, 'Tickets available!')
    else:
        bot.sendMessage(chatID, 'Tickets NOT available!')
