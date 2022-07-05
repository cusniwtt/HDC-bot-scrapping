import os
import pandas as pd
from glob import glob

def index(path):
    input = str(path)
    index = 0
    for i in range(6):
        if input[i].isdigit():
            index = i
    return index + 2


all_path = glob('D:\Backup\Dataset_fix\*\*.csv')
for path in all_path:
    split = os.path.split(path)
    folder = str(split[0]) + '\\'
    filename = str(split[1])
    pos = index(filename)
    print(path + 'is change to ' + path[10:])
    os.rename(path, folder + filename[:pos] + path[-10:])
    print('Rename successfully')