
# 라이브러리 삽입
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup


# 메인 코드
baseurl = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'
plusurl = input('검색어를 입력하세요:')
url = baseurl+urllib.parse.quote_plus(plusurl)
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_='sh_blog_title')

for i in title:
    print(i.attrs['title'])
    print(i.attrs['href'])
