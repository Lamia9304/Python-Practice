import requests
from bs4 import BeautifulSoup
import re

# 함수


def Print():   # 출력 함수
    print(table)
    print(table2)
    print(dd_table1)
    print(dd_table2)
    print(btn_clear)
    print(file_list)
    print(land_view)
    print(view_imcha_clear)
    print(view_etc_ju_clear)
    print(clear)
    print(clear_view_trju_clear)


def clean_str(text):  # 문자열 태그 제거 함수
    text = re.sub('<[^>]*>', '', text, 0).strip()
    return text


def append(total_list, a_list):  # 리스트 추가 함수(이중 리스트 제작)
    total_list.append(a_list)
    return total_list


# 로그인에 필요한 정보들
LOGIN_DATA = {
    'client_id': 'magpass',
    'pwd_dummy': 'thepower'
}
LOGIN_URL = 'http://www.goodauction.com/'

# 세션 접속 후 페이지 이동
with requests.Session()as s:
    r = s.get(
        'http://www.goodauction.com/')
    res = s.post(LOGIN_URL, data=LOGIN_DATA)
    print(res)
    status = res.status_code
    print(status)
    url_page = s.get(
        'http://www.goodauction.com/auction/ca_view.php?product_id=1933925&sample_key=1')
    soup = BeautifulSoup(url_page.text, 'html.parser')


# 테이블 탐색

    table = clean_str(
        str(soup.find("div", class_="view_gibon clear"))).replace(" ", '')
    table = table.splitlines()
    table = ' '.join(table).split()

    # data = {table[0]: table[1], table[2]: table[3]}
    # print(data)

    # aa.append(table[0])
    # print(aa)
    # print(data)

    # print(data['소재지'])
    # Table = {}
    # data = []
    # data.append(table[10])

    # print(new_table)
    # print(table)   # 시설 정보

    table2 = clean_str(
        str(soup.find("td", class_="tbl_history center"))).replace(" ", '')
    table2 = table2.splitlines()
    table2 = ' '.join(table2).split()
    # 입찰 결과

    dd_table1 = clean_str(
        str(soup.find("table", id="dd_table_1"))).replace(" ", '')
    dd_table1 = dd_table1 .splitlines()
    dd_table1 = ' '.join(dd_table1).split()  # 건물 등기부

    dd_table2 = clean_str(
        str(soup.find("table", id="dd_table_2"))).replace(" ", '')
    dd_table2 = dd_table2 .splitlines()
    dd_table2 = ' '.join(dd_table2).split()  # 토지 등기부

    btn_clear = clean_str(
        str(soup.find("div", class_="view_btn clear no_print"))).replace(" ", '')
    btn_clear = btn_clear .splitlines()
    btn_clear = ' '.join(btn_clear).split()

    file_list = clean_str(str(
        soup.find("div", class_="view_btn clear no_print"))).replace(" ", '')
    file_list = file_list .splitlines()
    file_list = ' '.join(file_list).split()  # 사진 펼쳐보기

    land_view = clean_str(
        str(soup.find("div", id="land_view"))).replace(" ", '')
    land_view = land_view .splitlines()
    land_view = ' '.join(land_view).split()  # 매각토지.건물현황

    view_imcha_clear = clean_str(str(
        soup.find("div", class_="view_imcha clear"))).replace(" ", '')
    view_imcha_clear = view_imcha_clear .splitlines()
    view_imcha_clear = ' '.join(view_imcha_clear).split()    # 임차인현황

    view_etc_ju_clear = clean_str(str(
        soup.find("div", class_="view_etc_ju clear"))).replace(" ", '')
    view_etc_ju_clear = view_etc_ju_clear .splitlines()
    view_etc_ju_clear = ' '.join(view_etc_ju_clear).split()  # 관련정보

    clear = clean_str(str(soup.find("div", class_="clear"))).replace(" ", '')
    clear = clear .splitlines()
    clear = ' '.join(clear).split()  # 하단 각종 메뉴들

    clear_view_trju_clear = clean_str(str(soup.find(
        "div", class_="clear view_trju clear"))).replace(" ", '')
    clear_view_trju_clear = clear_view_trju_clear .splitlines()
    clear_view_trju_clear = ' '.join(
        clear_view_trju_clear).split()  # 지자체 정보 및 기타현황

    info = []
    variety = []
    total_table = []

    append(info, table[1])
    append(variety, table[3])
    append(total_table, info)
    append(total_table, variety)
    # append(total_table, table2)
    print(total_table)
    print(total_table[1])
# 테이블 출력
# Print()
