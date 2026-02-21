from flask import Flask, request
from telegram import Update, Bot
from telegram.ext.dispatcher import Dispatcher
from telegram.ext.commandhandler import CommandHandler
import os
import logging
import bot_handlers

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Initialize Bot and Dispatcher
TOKEN = os.environ.get('TG_BOT_TOKEN')
if not TOKEN:
    logger.error("TG_BOT_TOKEN environment variable not set!")

bot = Bot(token=TOKEN)

# Dispatcher setup for serverless
dispatcher = Dispatcher(bot, None, workers=0, use_context=True)

# Register handlers from shared module
dispatcher.add_handler(CommandHandler('meow', bot_handlers.meow))
dispatcher.add_handler(CommandHandler('start', bot_handlers.start))
dispatcher.add_handler(CommandHandler('fact', bot_handlers.fact))

@app.route('/', methods=['POST'])
def webhook():
    if request.method == "POST":
        json_update = request.get_json(force=True)
        update = Update.de_json(json_update, bot)
        dispatcher.process_update(update)
    return "ok"

@app.route('/', methods=['GET'])
def index():
    return "NotACatBot is running!"
