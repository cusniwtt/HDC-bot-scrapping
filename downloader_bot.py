from os import listdir
from os.path import isfile, join
from selenium import webdriver as wd
import time
import os
import shutil
import codecs

#Defind function to rename file csv
def rename_file(dir_path, name):
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

    for i in range(len(new)):
        #Create save path
        save_name = str('/' + name + '__' + year[i] + '.csv')
        save_path = dir_path + save_name

        #Save file to dataset folder
        shutil.move(new[i], save_path)

#For create log file
def write_log(name):
    log = codecs.open('log\download_log.txt', 'a', 'utf-8-sig')
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
def bot(url, delay_time):
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
        time.sleep(delay_time)      #Wait for query

        dl_btn = driver.find_element_by_xpath('//*[@id="save-icon"]/button')    #Click Download button
        dl_btn.click()

        csv_btn = driver.find_element_by_xpath('//*[@id="save-icon"]/ul/li[1]/a')   #Download csv file
        csv_btn.click()
        time.sleep(1)