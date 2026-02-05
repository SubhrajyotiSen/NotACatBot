from telegram.ext import Updater, CommandHandler
import os
import logging
import bot_handlers

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def main():
    token = os.environ.get('TG_BOT_TOKEN')
    if not token:
        print("Error: TG_BOT_TOKEN not set.")
        return

    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler('meow', bot_handlers.meow))
    dp.add_handler(CommandHandler('start', bot_handlers.start))
    dp.add_handler(CommandHandler('fact', bot_handlers.fact))
    
    print("Bot starting polling...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()