import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import re


def Table_Data(content):
    i = 0
    for tr in content:
        test_data = content[i].text()
        print(test_data)
        i += 1


driver = webdriver.Chrome()
url = 'http://www.dooinauction.com/auction/ca_view_free.php?product_id=2126268&sample_idx=1706'
driver.get(url)
html = driver.page_source
soup = bs(html, 'html.parser')

data = []


table = soup.find('table', {'class': 'tbl_box_title'})
table2 = soup.find_all('table', {'class': 'tbl_grid'})
tr_data = table.find_all('tr')


i = 0
for tr in tr_data:

    test_data = (tr_data[i].get_text())
    print(test_data)
    i += 1

j = 0
for trs in table2[j].find_all('tr'):
    trs = trs.find('tr').get_text()

    print(trs)
    j += 1


driver.close()


# for tr in tr_data:
#     ths = list(tr.find_all('th'))
#     tds = list(tr.find_all('td'))
#     print(ths, tds)


\
# for td in soup.find_all('td'):
#     print(td.get_text())


# driver.close(
# )

# for tr in data:
#     tds = list(tr.find_all('td'))
#     print(tds)


# # <table class="table_develop3">을 찾음
# table = soup.find('table', {'class': 'tbl_box_title'})
# data = []                            # 데이터를 저장할 리스트 생성
# for th in table.find_all('th'):      # 모든 <tr> 태그를 찾아서 반복(각 지점의 데이터를 가져옴)
#     tds = list(th.find_all('td'))    # 모든 <td> 태그를 찾아서 리스트로 만듦
#     # (각 날씨 값을 리스트로 만듦)
#     for td in tds:                   # <td> 태그 리스트 반복(각 날씨 값을 가져옴)
#         if td.find('a'):             # <td> 안에 <a> 태그가 있으면(지점인지 확인)
#             point = td.find('a').text    # <a> 태그 안에서 지점을 가져옴
#             temperature = tds[5].text    # <td> 태그 리스트의 여섯 번째(인덱스 5)에서 기온을 가져옴
#             humidity = tds[9].text       # <td> 태그 리스트의 열 번째(인덱스 9)에서 습도를 가져옴
#             # data 리스트에 지점, 기온, 습도를 추가
#             data.append([point, temperature, humidity])
