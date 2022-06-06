from downloader_bot import bot
from downloader_bot import check_slash
from downloader_bot import rename_file
from downloader_bot import write_log

import pandas as pd
from win10toast import ToastNotifier as tn

df = pd.read_csv('link_csv/tree_link_csv/defend_อนามัยโรงเรียน.csv', sep='|')
max = 29
row = 28

name = df.iloc[row-1][0]
url = df.iloc[row-1][1]
save_dir = 'C:/Users/USER/Downloads/Dataset/defend_อนามัยโรงเรียน'
#Check slash and replace it with 'or'
name = check_slash(name)
#run bot to download file
bot(url, 10)
#rename file csv that bot download at last
rename_file(save_dir, name)
#Create log of file that bot download is complete
write_log(name)
print('{} Created Successfully'.format(name))
print('from This URL: {}'.format(url))

noti = tn()
noti.show_toast('Download complete', name, duration=5)