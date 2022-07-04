import sqlite3
from sqlite3 import Error
from random import randint
import json

connection = sqlite3.connect('D:\SQLiteStudio\SQL_project.db')
cursor = connection.cursor()

chairs_add = []
lenst = len(cursor.fetchall())

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def chair_add(names):
    
    cursor.execute("SELECT * FROM chair")
    ch = cursor.fetchall()
    
    for i in range(len(names)):
        ch = names[i]
        cursor.execute("INSERT INTO chair (chair) VALUES (?)", (ch,))
        connection.commit()

def literature_add(names):

    keys_lits = key_chairs()

    keys = keys_lits[0]
    lits = keys_lits[1]

    for i in range(len(keys)):
        id = names.index(keys[i])
        cursor.execute("INSERT INTO literature(id, lit, num) VALUES (?, ?, ?)", (id+1, lits[i], i))
    connection.commit()

def key_chairs():
    keys = []
    lits = []

    with open('chairs.json') as f:
        file_content = f.read()
        templates = json.loads(file_content)

    for i in range(len(templates)):
        key = str(templates[i].keys())[12:-3]
        keys.append(key)

        lit = templates[i][key]
        lits.append(lit)
        

    return keys, lits

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
        records = list(records)
        new_records = records[num]
        new_records = new_records[::-1]
        check = [id, num]
        if check == new_records:
            print(records)

        cursor.close()

    except sqlite3.Error as error:
        print()
    finally:
        if connection:
            connection.close()
            print()
    return records[num][2]

def read_chair(id):
    try:
        connection = sqlite3.connect('D:\SQLiteStudio\SQL_project.db')
        cursor = connection.cursor()
        id = id-1
        cursor = connection.cursor()
        sqlite_select_query = """SELECT * FROM chair"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        cursor.close()

    except sqlite3.Error as error:
        print()
    finally:
        if connection:
            connection.close()
            print()
    return records[id][1]