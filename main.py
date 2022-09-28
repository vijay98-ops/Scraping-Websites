from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import json
import os
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import numpy as np

pages = np.arange
url_collected = []

for page in pages:
  page = "https://itti.com.np/"
  driver = webdriver.Chrome()
  driver.get(page)
  sleep(randint(5, 15))
  soup = BeautifulSoup(driver.page_source, 'html.parser')
  urls = [item.get("href") for item in soup.find_all("a")]

# remove duplicates and None Values
urls_final = list(dict.fromkeys(url_collected))
urls_final = list(filter(None, urls_final))

# remove if not starting with pwa, remove if ending with display=reviews
url_final = [x for x in urls_final if x.startswith('/pwa/')]
url_final = [x for x in url_final if not x.endswith('display=reviews')]

string = "https://itti.com.np"
final_string = [string + s for s in url_final]
