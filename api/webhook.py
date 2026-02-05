from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler
import requests
import random
import os
import datetime
import time

app = Flask(__name__)

TOKEN = os.environ.get('TG_BOT_TOKEN')
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot, None, workers=0)

def get_url():
    response = requests.get('https://api.thecatapi.com/v1/images/search').json()
    image_url = response[0]['url']
    return image_url

def meow(update, context):
    url = get_url()
    chat_id = update.message.chat_id
    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    log = '{} | {} | meow\n'.format(timestamp, chat_id)
    print(log)
    if (url.endswith('gif')):
        context.bot.send_animation(chat_id=chat_id, animation=url)
    else:
        context.bot.send_photo(chat_id=chat_id, photo=url)

def fact(update, context):
    url = "https://catfact.ninja/fact?max_length=200"
    chat_id = update.message.chat_id
    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    log = '{} | {} | fact\n'.format(timestamp, chat_id)
    print(log)
    response = requests.get(url).json()
    text = response['fact']
    context.bot.send_message(chat_id=chat_id, text=text)

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text='Let\'s start meow-ing')

dispatcher.add_handler(CommandHandler('meow', meow))
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('fact', fact))

@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'OK'

@app.route('/')
def index():
    return 'Bot is running!'
