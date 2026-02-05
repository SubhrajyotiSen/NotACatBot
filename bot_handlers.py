import requests
import datetime
import time
import logging

logger = logging.getLogger(__name__)

def get_url():
    try:
        response = requests.get('https://api.thecatapi.com/v1/images/search').json()
        image_url = response[0]['url']
        return image_url
    except Exception as e:
        logger.error(f"Error fetching cat image: {e}")
        return "https://http.cat/500" # Fallback

def meow(update, context):
    url = get_url()
    chat_id = update.effective_chat.id
    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    logger.info(f'{timestamp} | {chat_id} | meow')
    
    try:
        if (url.endswith('gif')):
            context.bot.send_animation(chat_id=chat_id, animation=url)
        else:
            context.bot.send_photo(chat_id=chat_id, photo=url)
    except Exception as e:
        logger.error(f"Error sending meow: {e}")
        context.bot.send_message(chat_id=chat_id, text="Sorry, no cat right now :(")

def fact(update, context):
    url = "https://catfact.ninja/fact?max_length=200"
    chat_id = update.effective_chat.id
    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    logger.info(f'{timestamp} | {chat_id} | fact')
    
    try:
        response = requests.get(url).json()
        text = response.get('fact', 'No fact found')
        context.bot.send_message(chat_id=chat_id, text=text)
    except Exception as e:
        logger.error(f"Error fetching fact: {e}")
        context.bot.send_message(chat_id=chat_id, text="Couldn't find a fact!")

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Let\'s start meow-ing')
