from selenium import webdriver as wd
import time

url = 'https://hdcservice.moph.go.th/hdc/main/index.php'
#url = 'https://hdcservice.moph.go.th/hdc/reports/report.php?source=pformated/format1.php&cat_id=f16421e617aed29602f9f09d951cce68&id=46914a29aebb9e55230cc408f59f2d39'
#url = 'https://google.com'
driver = wd.Edge('edgedriver_win64\msedgedriver.exe')
driver.get(url)
time.sleep(5)