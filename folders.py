import os

path = "D:\\Проект ЯП 3\\folders"

def create(name_folder):

    try:
        os.mkdir(f"D:\\Проект ЯП 3\\folders\\{name_folder}")
    except OSError:
        return ("Создать директорию %s не удалось. Возможно она уже существует, либо неверно указано имя директории" % name_folder)
    else:
        return ("Успешно создана директория %s " % name_folder)

# просмотр доступных директорий
def view_folders():

    return os.listdir(path)

# просмотр выбранной директории
def view_one_folder(dir):

    content = os.listdir(f'{path}\\{dir}')
    
    return content

# добавить файл в директорию
def add_file_in_folder():

    pass