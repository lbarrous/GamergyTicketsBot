import schedule

from gamergyBot import bot

# schedule crawler
schedule.every(5).seconds.do(bot)

# run script infinitely
while True:
    schedule.run_pending()
