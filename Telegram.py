from dis import dis
from email import message
import logging
import traceback
import telegram
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters, InlineQueryHandler
from xml.dom.minidom import Document
from telegram import Update, ParseMode, User
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters, InlineQueryHandler
from telegram.ext import CommandHandler
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler
from DB import read_literature, read_chair, regist_users, check_id
from folders import create, view_folders, view_one_folder

TOKEN = '5123928550:AAEXVFMdn5Q45eh37Yj4yT7Epa2QBa8bHl8'
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# функция обработки команды '/start'
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Бот является чисто учебным созданием. Он способен отправлять файлы по введенному коду. Для помощи введите /help")

# функция обработки команды '/help'
def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                            text = "Для скачивания введите /d 'код документа'")

# функция обработки команды '/d'
def caps(update, context):

    if context.args:
        text_caps = context.args[0]
        txt = text_caps.split("-")
        chair = read_literature(int(txt[0]), int(txt[1]))
        lit = read_chair(int(txt[0]))
        updater.bot.send_document(chat_id=update.message.chat.id,document=open(f"D:\\Проект ЯП 3\\Documents\\{lit}\\{chair}", "rb"))                
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                text='Неверный аргумент команды')

# функция обработки не распознных команд
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Неизвестная команда. Введите /help")

def error_handler(update, context):
    """
        Регистрирует ошибку и уведомляет   
        разработчика сообщением telegram.
    """
    # Пишем ошибку, прежде чем что-то делать. Вдруг что-то сломается.
    logger.error(msg="Исключение при обработке сообщения:", exc_info=context.error)

    # `traceback.format_exception` возвращает обычное сообщение python 
    # об исключении в виде списка строк, поэтому объединяем их вместе.
    tb_list = traceback.format_exception(None, context.error, context.error.__traceback__)
    tb_string = tb_list[-1]

    if "Errno 2" in tb_string:
        message = (f"Документ не найден, проверьте правильность введенного кода")
        
    elif "File must be non-empty" in tb_string:
        message = (f"Попытка скачать пустой документ") 

    else: message = (f'Неизвестная ошибка')

    # Отправляем сообщение разработчику
    context.bot.send_message(chat_id=update.message.chat.id, text=message, parse_mode=ParseMode.HTML)

# проверка root прав
def root(update, context):

    user_id = update.message.from_user
    check = check_id(user_id)
    if check==True:
        message = (f'У Вас есть root права')
    else: message = (f'У Вас нет root прав')

    context.bot.send_message(chat_id=update.message.chat.id, text=message, parse_mode=ParseMode.HTML)

# создание директории
def create_folder(update, context):

    if context.args:
        text_caps = context.args[0]
        
    message = create(text_caps)
    context.bot.send_message(chat_id=update.message.chat.id, text=message, parse_mode=ParseMode.HTML)

# добавить в директорию
def add_in_folder(update, context):

    pass

# список доступных директорий
def dir_folders(update, context):

    message = view_folders()

    for i in range(len(message)):
        context.bot.send_message(chat_id=update.message.chat.id, text=message[i], parse_mode=ParseMode.HTML)

# список файлов в директории
def one_folder(update, context):

    if context.args:
        text_caps = context.args[0]

    message = view_one_folder(text_caps)

    for i in range(len(message)):
        context.bot.send_message(chat_id=update.message.chat.id, text=message[i], parse_mode=ParseMode.HTML)

# регистрация пользователя
def reg_user(update, context):

    user_id = update.message.from_user
    
    check = check_id(user_id)

    if check==True:
        message = (f'Вы уже зарегистрированы')
        context.bot.send_message(chat_id=update.message.chat.id, text=message, parse_mode=ParseMode.HTML)
    else: 
        message = (f'Вы не зарегистрированы, сейчас мы это исправим')
        context.bot.send_message(chat_id=update.message.chat.id, text=message, parse_mode=ParseMode.HTML)
        regist_users(user_id["id"])
        message = (f'Готово')
        context.bot.send_message(chat_id=update.message.chat.id, text=message, parse_mode=ParseMode.HTML)
    return True

if __name__ == '__main__':

    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # регистрация пользователя
    regist_user = CommandHandler('reg', reg_user)
    dispatcher.add_handler(regist_user)

    # Создание папки
    create_fold = CommandHandler('create', create_folder)
    dispatcher.add_handler(create_fold)

    # Просмотр содержимого директории
    view_dir = CommandHandler('view_one', one_folder)
    dispatcher.add_handler(view_dir)

    # просмотр директорий
    view = CommandHandler('view', dir_folders)
    dispatcher.add_handler(view)

    # проверка root прав
    roots = CommandHandler('root', root)
    dispatcher.add_handler(roots)

    # ...и обработчик ошибок
    dispatcher.add_error_handler(error_handler)

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # обработчик команды '/help'
    help_handler = CommandHandler('help', help)
    dispatcher.add_handler(help_handler)  

    # обработчик команды '/d'
    caps_handler = CommandHandler('d', caps)
    dispatcher.add_handler(caps_handler)

    # обработчик не распознных команд
    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)

    # Запускаем бота
    updater.start_polling()
    updater.idle()