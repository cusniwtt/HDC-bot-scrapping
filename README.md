# HDC-bot-scrapping
Bot to scrap csv file in all category in https://hdcservice.moph.go.th/hdc/main/index.php

## Prerequisite
1. **Microsoft Edge Version 102.0.1245.33 (Official build) (64-bit)** or EdgeWebDriver in same version in your computer. Because I use Microsoft Edge and in this repo give you EdgeWebDriver. If you use chrome or firefox etc.. You can download WebDriver same as your web browser </br>
For EdgeWebDriver : https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
2. **Python 3.7 up** (I use Python 3.10 Windows Store) </br>
3. I prefer Windows 10 or 11 to run this project. (Because i use it.) It maybe have a problem about path in this apps. (Differentation about path in Windows and Linux or MacOS system)
---
## Install supplement library
This apps requires all of this library. 
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all of it </br> </br>
For install [requests](https://pypi.org/project/requests/) to get url
```bash
pip install requests
```
For Install [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to get html
```bash
pip install bs4
```
For install [Selenium](https://selenium-python.readthedocs.io/) to create bot download
```bash
pip install selenium
```
For install [Pandas](https://pandas.pydata.org/) to generate csv link
```bash
pip install pandas
```
For install [tqdm](https://tqdm.github.io/) to crreat progress bar
```bash
pip install tqdm
```
For install [win10toast](https://pypi.org/project/win10toast/) to notify "Your download is successful"
```bash
pip install win10toast
```
---
