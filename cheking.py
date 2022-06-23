from YandexDisk import *
from Path import *

kol_vo = len(path_in_holder())

for i in range(kol_vo):
    file = path_in_holder()[i]
    dl_file(file)