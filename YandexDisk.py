from numpy import character
import yadisk
import pickle
from pathlib import Path
import json

y = yadisk.YaDisk(token='AQAAAAAT_OoiAADLW9gGFT5KI0gFvFYOzyvLsso')

liter = []

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

def chairs_list():
    chairs = []
    
    lens = len(list(y.listdir('disk:/Metodichka')))

    for i in range(lens):
        chair = list(y.listdir('disk:/Metodichka'))
        chairs.append(chair[i]['name'])
        
    return chairs

chair = chairs_list()
chair_one_new = []

def literature_list():
    file_name = "chairs.json"
    # with open("chairs.json", "w") as f:
    #     pass
    for i in range(len(chair)):
        chair_one_len = len(list(y.listdir(f'disk:/Metodichka/{chair[i]}')))
        for j in range(chair_one_len):
            if chair[i]=='AIS':
                chair_one = list(y.listdir(f'disk:/Metodichka/{chair[i]}'))
                files = chair_one[j]['name']
                to_json = {chair[i]: files}

                with open(file_name, "r") as file:
                    data = json.load(file)

                data.append(to_json)

                with open(file_name, "w") as file:
                    json.dump(data, file,indent=4)

            elif chair[i]=='Admin_Activ':
                chair_one = list(y.listdir(f'disk:/Metodichka/{chair[i]}'))
                files = chair_one[j]['name']
                to_json = {chair[i]: files}

                with open(file_name, "r") as file:
                    data = json.load(file)

                data.append(to_json)

                with open(file_name, "w") as file:
                    json.dump(data, file,indent=4)
            elif chair[i]=='Admin_Law':
                chair_one = list(y.listdir(f'disk:/Metodichka/{chair[i]}'))
                files = chair_one[j]['name']
                to_json = {chair[i]: files}

                with open(file_name, "r") as file:
                    data = json.load(file)

                data.append(to_json)

                with open(file_name, "w") as file:
                    json.dump(data, file,indent=4)
            elif chair[i]=='RESaSMC':
                chair_one = list(y.listdir(f'disk:/Metodichka/{chair[i]}'))
                files = chair_one[j]['name']
                to_json = {chair[i]: files}

                with open(file_name, "r") as file:
                    data = json.load(file)

                data.append(to_json)

                with open(file_name, "w") as file:
                    json.dump(data, file,indent=4)
            elif chair[i]=='Math':
                chair_one = list(y.listdir(f'disk:/Metodichka/{chair[i]}'))
                files = chair_one[j]['name']
                to_json = {chair[i]: files}

                with open(file_name, "r") as file:
                    data = json.load(file)

                data.append(to_json)

                with open(file_name, "w") as file:
                    json.dump(data, file,indent=4)
            elif chair[i]=='Ru_and_Foreign':
                chair_one = list(y.listdir(f'disk:/Metodichka/{chair[i]}'))
                files = chair_one[j]['name']
                to_json = {chair[i]: files}

                with open(file_name, "r") as file:
                    data = json.load(file)

                data.append(to_json)

                with open(file_name, "w") as file:
                    json.dump(data, file,indent=4)
            elif chair[i]=='Info_SaT':
                chair_one = list(y.listdir(f'disk:/Metodichka/{chair[i]}'))
                files = chair_one[j]['name']
                to_json = {chair[i]: files}

                with open(file_name, "r") as file:
                    data = json.load(file)

                data.append(to_json)

                with open(file_name, "w") as file:
                    json.dump(data, file,indent=4)
            elif chair[i]=='Info_Sec':
                chair_one = list(y.listdir(f'disk:/Metodichka/{chair[i]}'))
                files = chair_one[j]['name']
                to_json = {chair[i]: files}

                with open(file_name, "r") as file:
                    data = json.load(file)

                data.append(to_json)

                with open(file_name, "w") as file:
                    json.dump(data, file,indent=4)
            elif chair[i]=='Crime':
                chair_one = list(y.listdir(f'disk:/Metodichka/{chair[i]}'))
                files = chair_one[j]['name']
                to_json = {chair[i]: files}

                with open(file_name, "r") as file:
                    data = json.load(file)

                data.append(to_json)

                with open(file_name, "w") as file:
                    json.dump(data, file,indent=4)
            elif chair[i]=='Fire_train':
                chair_one = list(y.listdir(f'disk:/Metodichka/{chair[i]}'))
                files = chair_one[j]['name']
                to_json = {chair[i]: files}

                with open(file_name, "r") as file:
                    data = json.load(file)

                data.append(to_json)

                with open(file_name, "w") as file:
                    json.dump(data, file,indent=4)
            elif chair[i]=='OperInvActiv':
                chair_one = list(y.listdir(f'disk:/Metodichka/{chair[i]}'))
                files = chair_one[j]['name']
                to_json = {chair[i]: files}

                with open(file_name, "r") as file:
                    data = json.load(file)

                data.append(to_json)

                with open(file_name, "w") as file:
                    json.dump(data, file,indent=4)
            elif chair[i]=='Psych_and_Ped':
                chair_one = list(y.listdir(f'disk:/Metodichka/{chair[i]}'))
                files = chair_one[j]['name']
                to_json = {chair[i]: files}

                with open(file_name, "r") as file:
                    data = json.load(file)

                data.append(to_json)

                with open(file_name, "w") as file:
                    json.dump(data, file,indent=4)
            elif chair[i]=='Com_Sec_and_Tech_Exp':
                chair_one = list(y.listdir(f'disk:/Metodichka/{chair[i]}'))
                files = chair_one[j]['name']
                to_json = {chair[i]: files}

                with open(file_name, "r") as file:
                    data = json.load(file)

                data.append(to_json)

                with open(file_name, "w") as file:
                    json.dump(data, file,indent=4)
            elif chair[i]=='Soc_Hum_Eco_Leg_discip':
                chair_one = list(y.listdir(f'disk:/Metodichka/{chair[i]}'))
                files = chair_one[j]['name']
                to_json = {chair[i]: files}

                with open(file_name, "r") as file:
                    data = json.load(file)

                data.append(to_json)

                with open(file_name, "w") as file:
                    json.dump(data, file,indent=4)
            elif chair[i]=='TST':
                chair_one = list(y.listdir(f'disk:/Metodichka/{chair[i]}'))
                files = chair_one[j]['name']
                to_json = {chair[i]: files}

                with open(file_name, "r") as file:
                    data = json.load(file)

                data.append(to_json)

                with open(file_name, "w") as file:
                    json.dump(data, file,indent=4)
            elif chair[i]=='THSL':
                chair_one = list(y.listdir(f'disk:/Metodichka/{chair[i]}'))
                files = chair_one[j]['name']
                to_json = {chair[i]: files}

                with open(file_name, "r") as file:
                    data = json.load(file)

                data.append(to_json)

                with open(file_name, "w") as file:
                    json.dump(data, file,indent=4)
            elif chair[i]=='CrimeLaw_and_Criminilogy':
                chair_one = list(y.listdir(f'disk:/Metodichka/{chair[i]}'))
                files = chair_one[j]['name']
                to_json = {chair[i]: files}

                with open(file_name, "r") as file:
                    data = json.load(file)

                data.append(to_json)

                with open(file_name, "w") as file:
                    json.dump(data, file,indent=4)
            elif chair[i]=='Crim_proc':
                chair_one = list(y.listdir(f'disk:/Metodichka/{chair[i]}'))
                files = chair_one[j]['name']
                to_json = {chair[i]: files}

                with open(file_name, "r") as file:
                    data = json.load(file)

                data.append(to_json)

                with open(file_name, "w") as file:
                    json.dump(data, file,indent=4)
            elif chair[i]=='PT':
                chair_one = list(y.listdir(f'disk:/Metodichka/{chair[i]}'))
                files = chair_one[j]['name']
                to_json = {chair[i]: files}

                with open(file_name, "r") as file:
                    data = json.load(file)

                data.append(to_json)

                with open(file_name, "w") as file:
                    json.dump(data, file,indent=4)
            elif chair[i]=='Physics_and_RE':
                chair_one = list(y.listdir(f'disk:/Metodichka/{chair[i]}'))
                files = chair_one[j]['name']
                to_json = {chair[i]: files}

                with open(file_name, "r") as file:
                    data = json.load(file)

                data.append(to_json)

                with open(file_name, "w") as file:
                    json.dump(data, file,indent=4)
    
                # with open("chairs.json", "w") as write_file:
                #     json.dump(Physics_and_RE, write_file, indent=4)
                # print(type(files))
            # liter.append(file)

    # return liter



def dl_file():

    for i in range(len(chair)):
        chair_one_len = len(list(y.listdir(f'disk:/Metodichka/{chair[i]}')))
        for j in range(chair_one_len):
            chair_one = list(y.listdir(f'disk:/Metodichka/{chair[i]}'))
            file = chair_one[j]['name']
            name = f'C:\\Users\\ThanDoma v2.0\\Desktop\\Проект ЯП 3\\Documents\\{chair[i]}\\{file}'
            y.download(f'disk:/Metodichka/{chair[i]}/{file}', (name))



literature_list()
# dl_file()