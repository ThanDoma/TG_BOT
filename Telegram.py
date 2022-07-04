from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters, InlineQueryHandler
from xml.dom.minidom import Document
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters, InlineQueryHandler
from telegram.ext import CommandHandler
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler
from DB import read_literature

TOKEN = '5123928550:AAEXVFMdn5Q45eh37Yj4yT7Epa2QBa8bHl8'
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

def chair(update, context):
    pass

# функция обработки команды '/start'
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="I'm a bot, please talk to me!")

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                            text = "Для скачивания введите /caps 'код документа'")

# функция обработки команды '/caps'
def caps(update, context):

    

    literature = read_literature
    if context.args:
        text_caps = context.args[0]
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                text=text_caps)
        updater.bot.send_document(chat_id=update.message.chat.id,document=open(f"C:\\Users\\ThanDoma v2.0\\Desktop\\Проект ЯП 3\\Documents\\{literature_sourse()[0][int(text_caps)]}", "rb"))                
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                text='No command argument')
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                text='send: /caps argument')

# функция обработки не распознных команд
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Sorry, I didn't understand that command.")

# обработчик команды '/start'
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

#обработчик команды '/chair'
chair_handler = CommandHandler('chair', chair)
dispatcher.add_handler(chair_handler)  

# обработчик команды '/help'
help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)  

# обработчик команды '/caps'
caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

# обработчик не распознных команд
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

# запуск прослушивания сообщений
updater.start_polling()

# обработчик нажатия Ctrl+C
updater.idle()