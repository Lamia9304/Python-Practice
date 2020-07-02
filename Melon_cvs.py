import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from selenium import webdriver
import csv

hdr = {'User-Agent': ' Mozilla/5.0'}
url = 'https: // www.melon.com/chart/index.htm'
req = urllib.request.Request(url, headers=hdr)
html = urllib.request.urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')

print(soup)
