from downloader_bot import bot
from downloader_bot import check_slash
from downloader_bot import rename_file
from downloader_bot import write_log

import pandas as pd
import numpy as np
import os
from os import listdir
from os.path import isfile, join

#Get path of csv file
csv_path = [f for f in listdir('link_csv/tree_link_csv') if isfile(join('link_csv/tree_link_csv', f))]
for path in csv_path:
	if 'access_การบำบัดรักษาและฟื้นฟูผู้ติดยาเสพติดจากระบบ_บสต.csv' == path:
			df = pd.read_csv('link_csv/tree_link_csv/{}'.format(path), sep='|')
			#Create sub directory
			parent_dir = 'C:/Users/USER/Downloads/Dataset/'
			dir_path = os.path.join(parent_dir, path[:-4])
			os.mkdir(dir_path)

			#Loop for each row in df that create from path
			for i in range(df.shape[0]):
				name = str(df.iloc[i][0])
				url = str(df.iloc[i][1])

				#Check slash and replace it with 'or'
				name = check_slash(name)

				#run bot to download file
				bot(url)

				#rename file csv that bot download at last
				rename_file(dir_path, name)

				#Create log of file that bot download is complete
				write_log(name)