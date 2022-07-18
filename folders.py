import os

path = "D:\\Проект ЯП 3\\folders"

def create(name_folder):

    try:
        os.mkdir(f"D:\\Проект ЯП 3\\folders\\{name_folder}")
    except OSError:
        return ("Создать директорию %s не удалось. Возможно она уже существует, либо неверно указано имя директории" % name_folder)
    else:
        return ("Успешно создана директория %s " % name_folder)
    
def view_folders():

    return os.listdir(path)

def view_one_folder():

    pass

def add_file_in_folder():

    pass