from selenium import webdriver as wd
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import requests

#to grab all link that contain in the page
def grab_all_link(url, filename):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    f = open(str(filename), "w")
    # traverse paragraphs from soup
    for link in soup.find_all("a"):
        data = link.get('href')
        f.write(data)
        f.write("\n")
    f.close()
    return print("Done")

url = 'https://hdcservice.moph.go.th/hdc/main/index.php'
grab_all_link(url, 'All_link.txt')
