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

url = 'https://hdcservice.moph.go.th/hdc/main/index.php'
driver = wd.Edge('edgedriver_win64\msedgedriver.exe')
driver.get(url)
time.sleep(5)