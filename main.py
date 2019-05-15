from telegram.ext import Updater, CommandHandler
import requests
import re
import random
import os

def get_url():
    random_number = random.randint(1,2)
    if (random_number == 1):
        image_url = requests.get('http://aws.random.cat/meow').json()['file']
    else:
        response = requests.get('https://api.thecatapi.com/v1/images/search').json()
        image_url = response[0]['url']
    return image_url

def meow(bot, update):
    url = get_url()
    print(url)
    chat_id = update.message.chat_id
    if (url.endswith('gif')):
        bot.send_animation(chat_id=chat_id, animation=url)
    else:
        bot.send_photo(chat_id=chat_id, photo=url)


def start(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text='Let\'s start meow-ing')

def main():
    updater = Updater(os.environ['TG_BOT_TOKEN'])
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('meow',meow))
    dp.add_handler(CommandHandler('start',start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
