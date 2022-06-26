from turtle import update
from xml.dom.minidom import Document
from telegram import Update
from telegram import ReplyKeyboardRemove
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler
from YandexDisk import list_sourse

button_help = 'Помощь'
button_spisok = 'Список'
button_pre_download = 'Скачать'
button_download = 'Скачать'
# ----------------------------------------------------------------------------------------------------------
def button_pre_download_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Введите код "',
    )
    
    # button_pre_download_handler(chat_id=update.message.chat_id[-1], context=context)
# ----------------------------------------------------------------------------------------------------------
def button_download_handler(chat_id, context: CallbackContext):
        updater = Updater(
            token = '5123928550:AAEXVFMdn5Q45eh37Yj4yT7Epa2QBa8bHl8',
            use_context=True
    )
        text = update.message.text()
        updater.bot.send_document(chat_id=chat_id,document=open(f"C:\\Users\\ThanDoma v2.0\\Desktop\\Проект ЯП 3\\Documents\\{list_sourse()[0][text[-1]]}", "rb"))
# ----------------------------------------------------------------------------------------------------------
def button_spisok_handler(update: Update, context: CallbackContext):

    lens = list_sourse()[1]
    for j in range(lens):
        update.message.reply_text(        
            text=f'{j+1}. {list_sourse()[0][j]}',
    )
# ----------------------------------------------------------------------------------------------------------
def button_help_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Кнопка "Список" выдает список доступной литературы',
    )
    update.message.reply_text(
        text='Кнопка "Скачать" скачивает выбранный файл',
        # reply_markup=ReplyKeyboardRemove(),
    )
# ----------------------------------------------------------------------------------------------------------
def message_handler(update: Update, context: CallbackContext):

    text = update.message.text

    if text.lower() == button_help.lower():
        return button_help_handler(update=update, context=context)
    elif text.lower() == button_spisok.lower():
        return button_spisok_handler(update=update, context=context)
    elif text.lower() == button_pre_download.lower():
        return button_pre_download_handler(update=update, context=context)
    elif text.lower() == button_download.lower():
        return button_download_handler(update=update, context=context)

    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_help)
            ],
            [
                KeyboardButton(text=button_spisok)
            ],
            [
                KeyboardButton(text=button_download)
            ]
        ],
        resize_keyboard=True,
    )

    update.message.reply_text(
        text='Нажми на кнопку ниже', 
        reply_markup=reply_markup
    )
# ----------------------------------------------------------------------------------------------------------
def main():
    print('Start')

    updater = Updater(
        token = '5123928550:AAEXVFMdn5Q45eh37Yj4yT7Epa2QBa8bHl8',
        use_context=True
    )

    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))

    updater.start_polling()
    updater.idle()      
# ----------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()