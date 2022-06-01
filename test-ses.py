from unicodedata import name
import requests
from bs4 import BeautifulSoup
import pandas as pd

def index_bracket(text):
    for c in text:
        if c == '<':
            first = text.index(c)
        if c == '>':
            second = text.index(c)
            return first, second
    return print('Null')

url = 'https://hdcservice.moph.go.th/hdc/main/index.php'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
names = soup.find_all('a')  # find all names

for i in range(len(names)):
    print(names[i])


urls = []

for link in soup.find_all('a'):
    full_url = 'https://hdcservice.moph.go.th/hdc/' + link.get('href')
    urls.append(link.get('href'))

df_names = pd.DataFrame(names, columns=['name'])
df_urls = pd.DataFrame(urls, columns=['url'])
df = pd.concat([df_names, df_urls], axis=1)

print(df.head(10))

#df.to_csv('All_link.csv', sep='|', index=False)