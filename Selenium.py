from bs4 import BeautifulSoup
from selenium import webdriver

from urllib.parse import quote_plus

baseUrl = 'https://www.google.com/search?q='
plusUrl = input('무엇을 검색할까요 : ')
url = baseUrl+quote_plus(plusUrl)

driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html)
r = soup.select('.r')
print(type(r))
for i in r:
    print(i.select_one('.LC20lbDKV0Md').text)
    print()

    driver.close()
