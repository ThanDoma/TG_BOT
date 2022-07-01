from ast import Num
import sqlite3




def read_chairs(id):
    try:
        connection = sqlite3.connect('D:\SQLiteStudio\SQL_project.db')
        cursor = connection.cursor()
        print("Подключен к SQLite")

        cursor = connection.cursor()
        sqlite_select_query = """SELECT * FROM chair"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Всего строк:  ", len(records))
        print(records[id][1])

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if connection:
            connection.close()
            print("Соединение с SQLite закрыто")


def read_literature(id, num):
    try:
        connection = sqlite3.connect('D:\SQLiteStudio\SQL_project.db')
        cursor = connection.cursor()
        print("Подключен к SQLite")
        id = id
        num = num
        cursor = connection.cursor()
        # sqlite_select_query = ""SELECT id, num FROM literature""
        cursor.execute("SELECT id, num FROM literature", (id, num))
        records = cursor.fetchall()
        print("Всего строк:  ", len(records))
        print(records)

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if connection:
            connection.close()
            print("Соединение с SQLite закрыто")

id = int(input())
num = int(input())
read_literature(id-1, num)