import encodings
import pandas as pd
import numpy as np
import statistics as stat
import csv
from glob import glob
from tqdm import tqdm
import os

def fix_dimension(filepath):
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        column = 0
        lenght = []
        array = []
        print('\n---------------------------\n {}'.format(filepath))
        for row in spamreader:
            lenght.append(len(row))
            temp = []
            for item in row:
                if ',' in item:
                    item = str(item.replace(',',''))
                temp.append(item)
            array.append(temp)
        print('Create new list from csv')
        column = max(lenght)  
        index = 0
        for row in array:
            if len(array) == column:
                break;
            index += 1  
        for i in range(index):
            col = len(array[i])
            while col < column:
                array[i].append('')
                col = len(array[i])
        print('Fill blank with [spacebar]')
        print('Max column is {}'.format(column))  
        filename = os.path.split(filepath)
        folder_name = os.path.split(filename[0])
        save_root = 'C:/Users/USER/Downloads/Dataset_fix/'
        df = pd.DataFrame(array)
        print('Create datafram with {} column'.format(column))
        df.to_csv(save_root + folder_name[1] + '/' + filename[1], sep='|', header=False, index=False)
        print('Successfully save dataframe to csv with delimeter = | \n---------------------------')

folder_path = os.listdir('C:/Users/USER/Downloads/Dataset/')

for f in folder_path:
    os.mkdir('C:/Users/USER/Downloads/Dataset_fix/' + f)
    filepath = sorted(glob('C:/Users/USER/Downloads/Dataset/' + f + '/*.csv'))
    for file in filepath:
        temp = os.path.split(file)
        full_path = temp[0] + '/' + temp[1]
        fix_dimension(full_path)
