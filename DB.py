import sqlite3
from sqlite3 import Error
from YandexDisk import chairs_list, literature_list

connection = sqlite3.connect('D:\SQLiteStudio\SQL_project.db')
cursor = connection.cursor()
cur = cursor.execute("SELECT * FROM chair")

chairs = chairs_list()
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

literature = literature_list()
liter_add = []
len_lit = len(cursor.fetchall())
import yadisk


def chair_add():
    
    cursor.execute("SELECT * FROM chair")
    chairs_add = chairs
    ch = cursor.fetchall()
    
    for i in range(lenst):
        if ch[i][0] in chairs:
            chairs_add.remove(ch[i][0])

    
    for i in range(len(chairs_add)):
        chairs_add.append(str(chairs_add[i]))
        ch = chairs_add[i]
        cursor.execute("INSERT INTO chair (chair) VALUES (?)", (ch,))
        connection.commit()

def literature_add():

    cursor.execute("SELECT * FROM literature")
    liter_add = literature
    lit = cursor.fetchall()

    for i in range(len_lit):
        pass

def add():
    pass

# def literature_add():
    
#     cursor.execute("SELECT * FROM chair")
#     chairs_add = chairs
#     ch = cursor.fetchall()
    
#     for i in range(lenst):
#         if ch[i][0] in chairs:
#             chairs_add.remove(ch[i][0])

    
#     for i in range(len(chairs_add)):
#         chairs_add.append(str(chairs_add[i]))
#         ch = chairs_add[i]
#         cursor.execute("INSERT INTO chair (chair) VALUES (?)", (ch,))
#         connection.commit()

chair_add()


AIS = [] # Кафедра автоматизированных информационных систем органов внутренних дел
Admin_Activ = [] # Кафедра административной деятельности органов внутренних дел
Admin_Law = [] # Кафедра административного права
RESaSMC = [] # Кафедра радиотехнических систем и комплексов охранного мониторинга
Math = [] # Кафедра математики и моделирования систем
Ru_and_Foreign = [] # Кафедра русского и иностранных языков
Info_SaT = [] # Кафедра инфокоммуникационных систем и технологий
Info_Sec = [] # Кафедра информационной безопасности
Crime = [] # Кафедра криминалистики
Fire_train = [] # Кафедра огневой подготовки
OperInvActiv = [] # Кафедра оперативно-разыскной деятельности
Psych_and_Ped = [] # Кафедра психологии и педагогики
Com_Sec_and_Tech_Exp = [] # Кафедра компьютерной безопасности и технической экспертизы
Soc_Hum_Eco_Leg_discip = [] # Кафедра социально-гуманитарных, экономических и правовых дисциплин
TST = [] # Кафедра тактико-специальной подготовки
THSL = [] # Кафедра теории и истории государства и права
CrimeLaw_and_Criminilogy = [] # Кафедра уголовного права и криминологии
Crim_proc = [] # Кафедра уголовного процесса
PT = [] # Кафедра физической подготовки
Physics_and_RE = [] # Кафедра физики и радиоэлектроники           
