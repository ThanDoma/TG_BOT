import os
from unittest import result 
from YandexDisk import list_sourse

path = 'C:\\Users\\ThanDoma v2.0'
path = 'C:\\Users\\ThanDoma v2.0\\Desktop\\Проект ЯП 3\\Documents'
result = os.walk(path)
the_lack_of = []

def path_in_holder():
    path = 'C:\\Users\\ThanDoma v2.0\\Desktop\\Проект ЯП 3\\Documents'
    result = os.walk(path)
    lens = checking_files()[1]
    
    for i in range(lens):
        for el in os.walk(path):
            if list_sourse()[0][i] in el[2]:
                n=1
            else: the_lack_of.append(list_sourse()[0][i])
    return the_lack_of

def checking_files():
    b = list_sourse()[0]
    l = list_sourse()[1]
    return b, l