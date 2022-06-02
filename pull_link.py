from unicodedata import name
from numpy import full, full_like
import requests
from bs4 import BeautifulSoup
import pandas as pd

#Parameter Setting
url = 'https://hdcservice.moph.go.th/hdc/main/index.php'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
names = soup.find_all('a')  # find all names
names_cut = []
urls = []

#Find all text and links for append in names_cut and urls list
for link in soup.find_all('a'):
    cut = link.text
    names_cut.append(cut)

    full_url = str(link.get('href'))
    if str(full_url)[:2] == '..':       #check is link has .. in front fill https:// and merge it
        full_url = 'https://hdcservice.moph.go.th/hdc/' + full_url[3:]
    if str(full_url)[:4] == '/hdc':
        full_url = 'https://hdcservice.moph.go.th/hdc/' + full_url[5:]
    urls.append(full_url)

df_names = pd.DataFrame(names_cut, columns=['name'])    #Create dataframe for names
df_urls = pd.DataFrame(urls, columns=['url'])           #Create dataframe for urls
df = pd.concat([df_names, df_urls], axis=1)             #Concat dataframe

print(df.head(10))

df.to_csv('link_csv/All_link.csv', sep='|', index=False)         #Save dataframe to csv file