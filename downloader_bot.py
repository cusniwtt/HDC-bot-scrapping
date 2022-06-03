import csv
from bs4 import BeautifulSoup as bs
import requests as rq
import pandas as pd
import numpy as np
from os import listdir
from os.path import isfile, join
from selenium import webdriver as wd
import time
import os

#Defind function to rename file csv
def rename_file(url_path, name):
    year = ['2565', '2564', '2563', '2562', '2561', '2560', '2559', '2558', '2557', '2556']
    csv_path = [f for f in listdir('C:/Users/USER/Downloads') if isfile(join('C:/Users/USER/Downloads', f))]
    new_name = []
    for path in csv_path:  
        if path[:14] == 'exportData_HDC':
            serve = 'C:/Users/USER/Downloads/' + path
            new_name.append(serve)
    first = new_name[9:]
    back = new_name[:9]
    new = first + back
    print(new)

    for i in range(len(new)):
        os.rename(new[i], 'C:/Users/USER/Downloads/dataset/{}_{}_{}.csv'.format(url_path, name, year[i]))

#For create log file
def write_log(name):
    log = open('dataset\log.txt', 'a')
    log.write('{} \n'.format(name))
    log.close()

#Defind Function to check slash and replace it with 'or'
def check_slash(name):
	for i in range(len(name)):
		if name[i] == '/':
			first = name[:i]
			last = name[i+1:]
			name = first + ' or ' + last
	return name

#Create BOT to click download button
def bot(url):
    driver = wd.Edge('edgedriver_win64\msedgedriver.exe')
    driver.get(url)

    sp_set = driver.find_element_by_xpath('//*[@id="selSP"]')       #Select Service plan
    sp_set.click()
    sp_option = driver.find_element_by_xpath('//*[@id="selSP"]/option[3]')  #Select each Hospitel
    sp_option.click()
    pro_set = driver.find_element_by_xpath('//*[@id="selAllProv"]') #Select Province
    pro_set.click()
    pro_option = driver.find_element_by_xpath('//*[@id="selAllProv"]/option[2]')    #Select each Province
    pro_option.click()

    year_set = driver.find_element_by_xpath('//*[@id="selYear"]')       #Select Year
    year_set.click()
    
    for i in range(10):
        opt_xpath = '//*[@id="selYear"]/option[{}]'.format(i+1) #Get year by option
        year_option = driver.find_element_by_xpath(opt_xpath)   #Select each year
        year_option.click()
        ok_btn = driver.find_element_by_xpath('//*[@id="btnOkey"]') #click OK to query
        ok_btn.click()
        time.sleep(9)      #Wait for query

        dl_btn = driver.find_element_by_xpath('//*[@id="save-icon"]/button')    #Click Download button
        dl_btn.click()

        csv_btn = driver.find_element_by_xpath('//*[@id="save-icon"]/ul/li[1]/a')   #Download csv file
        csv_btn.click()
        time.sleep(1)

#Get path of csv file
csv_path = [f for f in listdir('link_csv/tree_link_csv') if isfile(join('link_csv/tree_link_csv', f))]

n = 0       #Set initial of amount file
for path in csv_path:       #Loop for each file in csv_path
    df = pd.read_csv('link_csv/tree_link_csv/{}'.format(path), sep='|')

    #Create Header of log by path of csv_path
    write_log('############################################################')
    write_log(path)
    write_log('############################################################')
    print('This is download file from {}'.format(path))

    #Loop for each row in df that create from path
    for i in range(df.shape[0]):
        name = df.iloc[i][0]        #Get name of url
        url = df.iloc[i][1]         #Get url

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