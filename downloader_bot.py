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
def rename_file(name):
    year = ['2565', '2564', '2563', '2562', '2561', '2560', '2559', '2558', '2557', '2556']
    csv_path = [f for f in listdir('dataset') if isfile(join('dataset', f))]
    new_name = []
    for path in csv_path:  
        if path[:14] == 'exportData_HDC':
            serve = 'D:/GitHub/HDC-bot-scrapping/dataset/' + path
            new_name.append(serve)
    first = new_name[9:]
    back = new_name[:9]
    new = first + back
    print(new)

    for i in range(10):
        os.rename(new[i], 'D:/GitHub/HDC-bot-scrapping/dataset/{}_{}.csv'.format(name, year[i]))

#Defind function to get year from url
def get_year(url):
    driver = wd.Edge('edgedriver_win64\msedgedriver.exe')
    driver.get(url)

    sp_set = driver.find_element_by_xpath('//*[@id="selSP"]')
    sp_set.click()
    sp_option = driver.find_element_by_xpath('//*[@id="selSP"]/option[3]')
    sp_option.click()
    pro_set = driver.find_element_by_xpath('//*[@id="selAllProv"]')
    pro_set.click()
    pro_option = driver.find_element_by_xpath('//*[@id="selAllProv"]/option[2]')
    pro_option.click()
    time.sleep(3)

    year_set = driver.find_element_by_xpath('//*[@id="selYear"]')
    year_set.click()
    
    for i in range(10):
        opt_xpath = '//*[@id="selYear"]/option[{}]'.format(i+1)
        year_option = driver.find_element_by_xpath(opt_xpath)
        year_option.click()
        ok_btn = driver.find_element_by_xpath('//*[@id="btnOkey"]')
        ok_btn.click()
        time.sleep(10)

        dl_btn = driver.find_element_by_xpath('//*[@id="save-icon"]/button')
        dl_btn.click()

        csv_btn = driver.find_element_by_xpath('//*[@id="save-icon"]/ul/li[1]/a')
        csv_btn.click()
        time.sleep(1)
    
    time.sleep(5)

#Get path of csv file
csv_path = [f for f in listdir('link_csv/tree_link_csv') if isfile(join('link_csv/tree_link_csv', f))]

#name = '1. รายงานสรุป CMI'
#get_year('https://hdcservice.moph.go.th/hdc/reports/report.php?source=pformated/format1.php&cat_id=833e9779725ef96bc06926d8ba4e4c04&id=ce331927a984726e907d00396cacda4d')
#rename_file(name)

n = 0
for path in csv_path:
    df = pd.read_csv('link_csv/tree_link_csv/{}'.format(path), sep='|')

    print('This is download file from {}'.format(path))

    for i in range(df.shape[0]):
        name = df.iloc[i][0]
        url = df.iloc[i][1]
        print(name)
        print(url)
        n = n + 1

print(n)
print(len(csv_path))