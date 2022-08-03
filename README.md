# HDC-bot-scrapping
Bot to scrap csv file in all category in https://hdcservice.moph.go.th/hdc/main/index.php </br></br>
For download dataset(ReLearning user): [HDC Dataset](https://thainhf.sharepoint.com/:f:/s/relearning/EgAN-vEOKhpDiiGdq9dUMScBcMOWo1JUwJ88YWbbv_Fyrg?e=fVGfCZ) </br></br>
If you are not in ReLearning. You can request to download at [it-support@relearninig.tech]

## Prerequisite
1. **Microsoft Edge Version 102.0.1245.33 (Official build) (64-bit)** or EdgeWebDriver in same version in your computer. Because I use Microsoft Edge and in this repo give you EdgeWebDriver. If you use chrome or firefox etc.. You can download WebDriver same as your web browser </br>
For EdgeWebDriver : https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
2. **Python 3.7 up** (I use Python 3.10 [Windows Store](https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5?hl=en-us&gl=US))
3. I prefer Windows 10 or 11 to run this project. (Because i use it.) It maybe have a problem about path in this apps and WebDriver. (Differentation about path in Windows and Linux or MacOS system)
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
## Understand the Website
Download path of https://hdcservice.moph.go.th/hdc/main/index.php is individually. That mean 1 indicator has 1 link. So, We need to look into structure and crawling all link that they have. </br>
This website has 2 level of path. First level is Category.(path in **All_link.csv**) This csv cannot use now. We need to split it by names of cactegory for detect easily. Second level is Indicator.(path in folder **tree_link_csv**) This .csv create by the same method as first level to get all download link.(indicator) </br>
In to the download site. We need to set some parameter to get my goal data. </br>
The parameter is:
* Year from 2556-2565 BE (2013-2022 AD)
* Service plan set to each hospital
* District set to each province
* File save in .csv format

## Methodology
1. Run **`pull_link.py`** to get all link in first level. 
   1. This code will use `BeautifulSoup` to find all `'a'` and add it to list.
   2. Use `pandas` to create dataframe from list that we create before.
   3. Use `pandas` to create .csv from dataframe name **'All_link.csv'**
2. Run **`fix_csv.py`** to split link into seperate .csv file by category.
3. Run **`pull_list_group_link.py`** to get all path for downloading. This do same thing that **`pull_link.py`** do but different level.
4. Run **`app.py`** to call bot function from `downloader_bot.py` to download. This app need index of rows that contain path of download.
   * Function `bot` has 2 input. First is url. Second is delay time.(default = 10s) You can change delay time if you feel slow or take time. But i recommend default is best.
   * Index is start from 1. You can check **`log/download_log.txt`** to compare what is right thing to do.
5. Run **`playground.py`** (Additional if **`app.py`** is return error) This is special case when you cannot run `app.py` propery. This playground need you few thing to download each rows of .csv
   * file name that you need to download appear in folder `tree_link_csv`
   * `max` is length of row in .csv
   * `row` is each row of index you need to download.
   * Default is enumerate, If you need to download specify file. You can remove loop and run it row by row.
