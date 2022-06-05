from selenium import webdriver as wd
import time

url = 'https://hdcservice.moph.go.th/hdc/main/index.php'
#url = 'https://google.com'
driver = wd.Edge('edgedriver_win64\msedgedriver.exe')
driver.get(url)
time.sleep(5)