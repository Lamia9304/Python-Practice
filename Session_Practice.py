import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
url = 'http://www.taein.co.kr/main1.html'
driver.get(url)
html = driver.page_source
soup = bs(html, 'html.parser')


# 로그인  접속 후 크롤링할 웹 페이지 접근

driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
Login_Id = driver.find_element_by_name('login_id').send_keys('magpass')
Login_Password = driver.find_element_by_name('login_password')


Login_Password.send_keys('magpass')
Login_Password.submit()
driver.maximize_window()
time.sleep(2)
driver.find_element_by_partial_link_text('이용안내').click()
driver.execute_script('window.scrollTo(0, 5000);')
driver.find_element_by_xpath('//*[@id="topNavi"]/li[4]/div/a').click()

# driver.find_element_by_xpath('//*[@id="con_center"]/div[4]/div[2]/a').click()


# for link in soup.find_all('a'):
#     print(link.get('href'))


# Login_Password = driver.find_element_by_name('login_password')
# Login_Password.send_keys('magpass')


# Login_Data = {
#     'login_id': 'magpass'
#     'login_password' 'magpass'

# }


# with requests.Session()as s:
#     frist_page = s.get('http: // www.taein.co.kr/')
#     html = frist_page.text
#     soup = bs(html, 'html.parser')


# login_req = s.post('www.taein.co.kr/', data=Login_Data)

# print(login_req.status_code)
