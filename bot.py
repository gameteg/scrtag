from telegram.ext import *

token="5200643131:AAEU5DKQ-mNWAd71S9wInwaLwAibYkiEOks"

def start(update, context) :
    update.message.reply_text("Hello, wellcome to my telegram bot")


def other_msg(update, context) :
    msg=update.message.text
    update.message.reply_text("I dont know about "+msg)

updater = Updater(token, use_context=True)

disp = updater.dispatcher


disp.add_handler(CommandHandler("start", start))
disp.add_handler(MessageHandler(Filters.text, other_msg))

updater.start_polling()
updater.idle()
