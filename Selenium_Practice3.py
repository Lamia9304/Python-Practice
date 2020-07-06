import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
url = 'https://www.naver.com/'
driver.get(url)
driver.maximize_window()
html = driver.page_source
soup = bs(html, 'html.parser')

driver.find_element_by_partial_link_text('웹툰').click()
