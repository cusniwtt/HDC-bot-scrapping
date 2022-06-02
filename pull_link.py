from unicodedata import name
from numpy import full, full_like
import requests
from bs4 import BeautifulSoup
import pandas as pd

def index_bracket(text):    #Defind function to find index of bracket
    for c in text:
        if c == '<':
            first = text.index(c)
        if c == '>':
            second = text.index(c)
            return first, second    #Return index of bracket
    first, second = 0, 0
    return first, second    #If null, return 0

url = 'https://hdcservice.moph.go.th/hdc/main/index.php'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
names = soup.find_all('a')  # find all names
names_cut = []

for i in range(len(names)): #Cut all names and append in names_cut list
    temp = str(names[i])[:-4]
    index1, index2 = index_bracket(temp)
    cut = temp[index2 + 1:]
    names_cut.append(cut)


urls = []

for link in soup.find_all('a'): #Find all links and append in urls list
    full_url = str(link.get('href'))
    if str(full_url)[:2] == '..':
        full_url = 'https://hdcservice.moph.go.th/hdc/' + full_url[3:]
    urls.append(full_url)

df_names = pd.DataFrame(names_cut, columns=['name'])    #Create dataframe for names
df_urls = pd.DataFrame(urls, columns=['url'])           #Create dataframe for urls
df = pd.concat([df_names, df_urls], axis=1)             #Concat dataframe

print(df.head(10))

df.to_csv('All_link.csv', sep='|', index=False)         #Save dataframe to csv file