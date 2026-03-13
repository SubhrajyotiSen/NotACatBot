from telegram.ext import Application, CommandHandler
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

    application = Application.builder().token(token).build()
    
    application.add_handler(CommandHandler('meow', bot_handlers.meow))
    application.add_handler(CommandHandler('start', bot_handlers.start))
    application.add_handler(CommandHandler('fact', bot_handlers.fact))
    
    print("Bot starting polling...")
    application.run_polling()

if __name__ == '__main__':
    main()
