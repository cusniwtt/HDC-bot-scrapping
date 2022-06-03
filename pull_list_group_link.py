from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup as bs
import requests as rq
import pandas as pd
import numpy as np

#Defind function to create dataframe from list group box
def list_group_box(path, name, url):
    reqs = rq.get(url)
    soup = bs(reqs.text, 'html.parser')
    names_cut = []
    urls = []
    flag =True

    #Check that web is single rows or category rows
    if soup.find_all('label', {'class': 'tree-toggler nav-header'}):
        flag = False

    if flag:    #If web is single rows
        #Find all names and append in names_cut list
        for link in soup.find_all('li', {'class': 'list-group-item row'}):
            cut = link.text
            names_cut.append(cut)
    else:       #If web is category rows
        #Find all names and append in names_cut list
        for link in soup.find_all('a'):
            cut = link.text
            if cut[4:5].isnumeric():    #Check is index is number
                names_cut.append(cut)
        del names_cut[:13]

    #Find all links and append in urls list
    for link in soup.find_all('a'):
        full_url = link.get('href')
        if str(full_url)[:6] == './../r':
            full_url = 'https://hdcservice.moph.go.th/hdc/' + full_url[5:]
            urls.append(full_url)

    df_names = pd.DataFrame(names_cut, columns=['name'])    #Create dataframe for names
    df_urls = pd.DataFrame(urls, columns=['url'])           #Create dataframe for urls
    df = pd.concat([df_names, df_urls], axis=1)             #Concat dataframe

    #Save dataframe to csv file
    df.to_csv('link_csv/tree_link_csv/{}_{}.csv'.format(path, name), sep='|', index=False, encoding='utf-8-sig') 

    return print('{}.csv created in tree_link_csv'.format(name))

#Get path of csv file
csv_path = [f for f in listdir('link_csv') if isfile(join('link_csv', f))]
del csv_path[1]
print(csv_path)

#For each csv file in csv_path
for name in csv_path:
    df = pd.read_csv('link_csv/{}'.format(name), sep='|')
    round = df.shape[0]

    #For each row in csv file
    for i in range(round):
        print('-----------------')
        list_group_box(name[:-4], df.iloc[i, 0], df.iloc[i, 1])
