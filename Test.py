from ast import Num
import sqlite3

def read_literature(id, num):
    try:
        connection = sqlite3.connect('D:\SQLiteStudio\SQL_project.db')
        cursor = connection.cursor()
        id = id
        num = num
        cursor = connection.cursor()
        sqlite_select_query = """SELECT * FROM literature"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        records = list(records[id])
        new_records = records[:2]
        check = [id, num]

        cursor.close()

    except sqlite3.Error as error:
        print()
    finally:
        if connection:
            connection.close()
            print()
    return records[2]

id = int(input())
num = int(input())
print(read_literature(num, id))