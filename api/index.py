from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler
import os
import logging
import asyncio
import bot_handlers

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

TOKEN = os.environ.get('TG_BOT_TOKEN')
if not TOKEN:
    logger.error("TG_BOT_TOKEN environment variable not set!")

async def _process_update(json_update):
    # Initialize application inside the request's event loop
    application = Application.builder().token(TOKEN).build()
    
    # Register handlers from shared module
    application.add_handler(CommandHandler('meow', bot_handlers.meow))
    application.add_handler(CommandHandler('start', bot_handlers.start))
    application.add_handler(CommandHandler('fact', bot_handlers.fact))

    await application.initialize()
    await application.start()
    update = Update.de_json(json_update, application.bot)
    await application.process_update(update)
    await application.stop()
    await application.shutdown()

@app.route('/', methods=['POST'])
def webhook():
    if request.method == "POST":
        json_update = request.get_json(force=True)
        asyncio.run(_process_update(json_update))
    return "ok"

@app.route('/', methods=['GET'])
def index():
    return "NotACatBot is running!"
