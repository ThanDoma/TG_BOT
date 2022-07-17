import sqlite3
from sqlite3 import Error
from random import randint
import json
from numpy import record

from regex import P

connection = sqlite3.connect('D:\SQLiteStudio\SQL_project.db', check_same_thread=False)
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

def create_table():
    cursor.execute("""CREATE TABLE chair(id INTEGER PRIMARY KEY AUTOINCREMENT, chair TEXT)""")
    cursor.execute("""CREATE TABLE literature(id INTEGER, num INTEGER NOT NULL, lit TEXT NOT NULL,
    FOREIGN KEY (id) REFERENCES chair(id))""")
    connection.commit()

def chair_add(names):
    
    cursor.execute("SELECT * FROM chair")
    ch = cursor.fetchall()
    
    for i in range(len(names)):
        ch = names[i]
        cursor.execute("INSERT INTO chair (chair) VALUES (?)", (ch,))
        connection.commit()

def regist_users(user_id):

    cursor.execute("SELECT * FROM regist_users")
    ch = user_id

    cursor.execute("INSERT INTO regist_users (id) VALUES (?)", (ch,))    
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

def check_id(user_id):
    k = 0
    try:
        cursor.connection.cursor()
        user_id = user_id
        sqlite_select_query = """SELECT * FROM regist_users"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        for i in range(len(records)):
            if user_id["id"]==records[i][0]:
                k+=1
                
    except sqlite3.Error as error:
        print()
    finally:
        if connection:
            print()

    if k==1:
        return True
    else: return False

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
            print()
    return records[id][1]