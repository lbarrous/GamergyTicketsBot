import schedule

from gamergyBot import bot

# schedule crawler
schedule.every(10).minutes.do(bot)

# run script infinitely
while True:
    schedule.run_pending()
