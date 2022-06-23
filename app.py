from downloader_bot import bot
from downloader_bot import check_slash
from downloader_bot import rename_file
from downloader_bot import write_log

import pandas as pd
from os import listdir
from os.path import isfile, join
from tqdm import tqdm
from win10toast import ToastNotifier as tn
import os

#Defind main app
def app(path):
    df = pd.read_csv('link_csv/tree_link_csv/{}'.format(path), sep='|')
    #Create sub directory
    parent_dir = 'C:/Users/USER/Downloads/Dataset/'
    dir_path = os.path.join(parent_dir, path[:-4])
    os.mkdir(dir_path)
    print('Create directory: {}'.format(dir_path))

    #Create Header of log by path of csv_path
    write_log('############################################################')
    write_log(path)
    write_log('############################################################')
    print('This is download file from {}'.format(path))

    #Loop for each row in df that create from path
    for i in tqdm(range(df.shape[0])):
        name = str(df.iloc[i][0])        #Get name of url
        url = str(df.iloc[i][1])         #Get url

        #Check slash and replace it with 'or'
        name = check_slash(name)

        #run bot to download file
        bot(url, 10)

        #rename file csv that bot download at last
        rename_file(dir_path, name)

        #Create log of file that bot download is complete
        write_log(name)
        print('{} Created Successfully'.format(name))
        print('from This URL: {}'.format(url))

#Get path of csv file
csv_path = [f for f in listdir('link_csv/tree_link_csv') if isfile(join('link_csv/tree_link_csv', f))]

#Set index of csv that send into app
index = 62
write_log('\n')
write_log('Index: {}'.format(index))

#Call app function
app(csv_path[index-1])

#Log Statement & Notification
first_row = 'Number of csv sub file: {} '.format(index)
last_row = 'of {}'.format(len(csv_path))
noti = tn()
noti.show_toast(csv_path[index-1] + 'Download Complete!!!', first_row + last_row, duration=5)