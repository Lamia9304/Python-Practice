from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome()
url = 'https://google.com'
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)

driver.find_element_by_css_selector('#gb_70').click()
action.send_keys('kanoring9304@gmail.com').perform()
driver.find_element_by_css_selector('.CwaK9').click()

driver.find_element_by_css_selector('.whsOnd.zHQkBf')
action.send_keys('animesample9').perform()
driver.find_element_by_css_selector('.CwaK9').click()
