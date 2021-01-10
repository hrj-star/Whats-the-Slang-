from selenium import webdriver
import getpass
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
from bs4 import BeautifulSoup as bs
import pandas as pd
import random
import csv
import requests
import json

def scrape():
    url = 'https://en.wiktionary.org/wiki/Appendix:English_internet_slang'
    r = requests.get(url) 
    soup = bs(r.content, 'lxml') 
   # print(soup.prettify())
    data = [] # create a list to store the items
    for div_secs in soup.find_all('div', {'class': 'mw-content-ltr'}):
        for slang_secs in div_secs.find_all('ul'):
            for slang in slang_secs.find_all('li'):
                data.append({"slang":slang.text.split(":")[0], "meaning": slang.text.split(":")[-1]})
               
                
               
                #print(slangword +":"+ slangmeaning)
                #data.append({"slang":slang[0].text, "meaning": slang[1].text})

    with open('data.txt', 'w') as f:
        json.dump(data, f)
        print("Done")
          


scrape()