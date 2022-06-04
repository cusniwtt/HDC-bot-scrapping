from downloader_bot import bot
from downloader_bot import check_slash
from downloader_bot import rename_file
from downloader_bot import write_log

import pandas as pd
import numpy as np
from os import listdir
from os.path import isfile, join
import os


#Get path of csv file
csv_path = [f for f in listdir('link_csv/tree_link_csv') if isfile(join('link_csv/tree_link_csv', f))]

n = 0       #Set initial of amount file
for path in csv_path:       #Loop for each file in csv_path
    df = pd.read_csv('link_csv/tree_link_csv/{}'.format(path), sep='|')
    #Create sub directory
    parent_dir = 'C:/Users/USER/Downloads/Dataset/'
    dir_path = os.path.join(parent_dir, path[:-4])
    os.mkdir(dir_path)

    #Create Header of log by path of csv_path
    write_log('############################################################')
    write_log(path)
    write_log('############################################################')
    print('This is download file from {}'.format(path))

    #Loop for each row in df that create from path
    for i in range(df.shape[0]):
        name = str(df.iloc[i][0])        #Get name of url
        url = str(df.iloc[i][1])         #Get url

        #Check slash and replace it with 'or'
        name = check_slash(name)

        #run bot to download file
        bot(url)

        #rename file csv that bot download at last
        rename_file(path, name)

        #Create log of file that bot download is complete
        write_log(name)
        print(name)
        print(url)
        n = n + 1

print('Number of file: {}'.format(n))
print('Number of CSV sub file: {}'.format(len(csv_path)))