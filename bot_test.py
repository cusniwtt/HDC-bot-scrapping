from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time

driver = wd.Edge(r"C:\Users\USER\Documents\edgedriver_win64\msedgedriver.exe")

driver.get('https://hdcservice.moph.go.th/hdc/main/index.php')

add1 = driver.find_element_by_xpath('//*[@id="navbar"]/ul[1]/li[2]/ul/li[1]/ul/li[1]/a')
add1.click()

time.sleep(10)
driver.quit()