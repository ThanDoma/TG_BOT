from numpy import character
import yadisk
from Test import *

y = yadisk.YaDisk(token='AQAAAAAT_OoiAADLW9gGFT5KI0gFvFYOzyvLsso')

liter = []



def chairs_list():
    chairs = []
    
    lens = len(list(y.listdir('disk:/Metodichka')))

    for i in range(lens):
        chair = list(y.listdir('disk:/Metodichka'))
        chairs.append(chair[i]['name'])

    return chairs

chair = chairs_list()
chair_one_new = []

def dl_file():

    for i in range(len(chair)):
        chair_one_len = len(list(y.listdir(f'disk:/Metodichka/{chair[i]}')))
        for j in range(chair_one_len):
            chair_one = list(y.listdir(f'disk:/Metodichka/{chair[i]}'))
            file = chair_one[j]['name']
            name = f'C:\\Users\\ThanDoma v2.0\\Desktop\\Проект ЯП 3\\Documents\\{chair[i]}\\{file}'
            y.download(f'disk:/Metodichka/{chair[i]}/{file}', (name))