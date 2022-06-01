from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time
import requests

from grablink import grab_all_link

url = 'https://hdcservice.moph.go.th/hdc/main/index.php'
driver = wd.Edge(r'edgedriver_win64\msedgedriver.exe')
driver.get(url)

NormRepbtn = driver.find_element_by_xpath('//*[@id="navbar"]/ul[1]/li[2]/a')
NormRepbtn.click()

time.sleep(5)
driver.quit()