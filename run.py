import YandexDisk
import DB

names = ["AIS", "Admin_Activ", "Admin_Law", "RESaSMC", "Math", "Ru_and_Foreign", "Info_SaT", "Info_Sec", "Fire_train", "Crime", "OperInvActiv", "Psych_and_Ped", "Com_Sec_and_Tech_Exp", "Soc_Hum_Eco_Leg_discip", "TST", "THSL", "CrimeLaw_and_Criminilogy", "Crim_proc", "PT", "Physics_and_RE"]
names.sort()

YandexDisk.dl_file()
YandexDisk.literature_list()
DB.chair_add(names)
DB.literature_add(names)