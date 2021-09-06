from pprint import pprint

import requests
from bs4 import BeautifulSoup


def getTicketsAvailability():
    # Create URL for gamergy website
    gamergySiteURL = 'https://www.ifema.es/gamergy/entradas-invitaciones'
    # Get page with request
    page = requests.get(gamergySiteURL)
    # Scrap the website to get tickets availability
    soup = BeautifulSoup(page.text, 'html.parser')
    try:
        try:
            sellingTicketsButtonClassesArray = soup.find(
                "a", {"class": "icon-users-1"}).get('class')
            ticketsAvailable = False if 'disabled' in sellingTicketsButtonClassesArray else True
            pprint(ticketsAvailable)
            return ticketsAvailable
        except:
            pprint('Selling tickets button not found!')
    except:
        pprint('Something went wrong...')


getTicketsAvailability()
