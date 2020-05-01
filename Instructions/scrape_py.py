from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import os
import time
import requests
import warnings
warnings.filterwarnings('ignore')

!which chromedriver

executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

#news
news_url = "https://mars.nasa.gov/news/"
browser.visit(news_url)

#html
html = browser.html

# parsing w bs
soup = bs(html, 'html.parser')

# pulling news title and paragraph
news = soup.find("div", class_='list_text')
news_title = news.find("div", class_="content_title").text
news_para = news.find("div", class_ ="article_teaser_body").text

#print
print(news_title)
print(news_para)