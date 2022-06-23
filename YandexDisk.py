import yadisk

y = yadisk.YaDisk(token='AQAAAAAT_OoiAADLW9gGFT5KI0gFvFYOzyvLsso')

#Цикл, создающий список литературы
def list_sourse():
    spisok = list(y.listdir('disk:/Metodichka'))
    d = list()
    lens = len(spisok)
    for i in range(lens):
        d.append(spisok[i]['name'])
    return d, lens


def dl_file(file):
    for i in range(list_sourse()[1]):
        name = f'C:\\Users\\ThanDoma v2.0\\Desktop\\Проект ЯП 3\\Documents\\{file}'
        y.download(f'disk:/Metodichka/{list_sourse()[0][i]}', (name))