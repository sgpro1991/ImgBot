from lib.telegram import bot
from multiprocessing import Pool


if __name__ == '__main__':
    pool = Pool(processes=10)
    bot.polling(none_stop=True, timeout=500000)


