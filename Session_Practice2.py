import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
url = 'http://lms.pknu.ac.kr/ilos/main/main_form.acl'
driver.get(url)
driver.maximize_window()
html = driver.page_source
soup = bs(html, 'html.parser')
driver.find_element_by_xpath(
    '//*[@id="top1m1"]/div/a').click()

driver.find_element_by_partial_link_text('비정규과목').click()
