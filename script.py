import telegram
from telegram.ext import CommandHandler, Updater

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I'm your bot!") 

updater = Updater(token='6129326217:AAHrd01-FDVNJ6ITXJ8lA8D2udJ4qfUeJoA', use_context=True)

dispatcher = updater.dispatcher 
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
