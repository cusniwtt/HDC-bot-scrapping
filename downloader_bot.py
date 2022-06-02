from bs4 import BeautifulSoup as bs
import requests as rq
import pandas as pd
import numpy as np
from os import listdir
from os.path import isfile, join

urls = 'https://hdcservice.moph.go.th/hdc/reports/report.php?source=pformated/format1.php&cat_id=9d8c311d6336373d40437c4423508cad&id=4b35d96e225bf34a16774b13705250f4'
reqs = rq.get(urls)
soup = bs(reqs.text, 'html.parser')

temp = []

for link in soup.find_all('a'):
    url = link.get('href')
    if 'CSV' in link.text:
        temp.append(url)
    cut = link.text

print(soup)
