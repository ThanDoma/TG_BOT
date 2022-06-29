import json

names = ["AIS", "Admin_Activ", "Admin_Law", "RESaSMC", "Math", "Ru_and_Foreign", "Info_SaT", "Info_Sec", "Fire_train", "Crime", "OperInvActiv", "Psych_and_Ped", "Com_Sec_and_Tech_Exp", "Soc_Hum_Eco_Leg_discip", "TST", "THSL", "CrimeLaw_and_Criminilogy", "Crim_proc", "PT", "Physics_and_RE"]

with open('chairs.json') as f:
    file_content = f.read()
    templates = json.loads(file_content)

print(templates)

for i in range(len(templates)):
    key = str(templates[i].keys())[12:-3]
    