import httpx
import datetime
import time
import logging
from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)

async def get_url():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get('https://api.thecatapi.com/v1/images/search')
            response.raise_for_status()
            image_url = response.json()[0]['url']
            return image_url
    except Exception as e:
        logger.error(f"Error fetching cat image: {e}")
        return "https://http.cat/500" # Fallback

async def meow(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = await get_url()
    chat_id = update.effective_chat.id
    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    logger.info(f'{timestamp} | {chat_id} | meow')
    
    try:
        if url.endswith('gif'):
            await context.bot.send_animation(chat_id=chat_id, animation=url)
        else:
            await context.bot.send_photo(chat_id=chat_id, photo=url)
    except Exception as e:
        logger.error(f"Error sending meow: {e}")
        await context.bot.send_message(chat_id=chat_id, text="Sorry, no cat right now :(")

async def fact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://catfact.ninja/fact?max_length=200"
    chat_id = update.effective_chat.id
    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    logger.info(f'{timestamp} | {chat_id} | fact')
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            text = response.json().get('fact', 'No fact found')
        await context.bot.send_message(chat_id=chat_id, text=text)
    except Exception as e:
        logger.error(f"Error fetching fact: {e}")
        await context.bot.send_message(chat_id=chat_id, text="Couldn't find a fact!")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Let\'s start meow-ing')
