# 라이브러리 불러오기
import requests
from bs4 import BeautifulSoup

# 검색 키워드

# 해당 url의 html문서를 soup 객체로 저장
url='https://kart.nexon.com/Kart/News/Patch/List.aspx'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')


search_result = soup.select('#kart_main_sections > section.board > div.board_inner > div.list_tb.tb_notice > table.tb_list > tbody > tr > td > div.list_td > div.tit_bx > a.txt_ellipsis')

for i in search_result:
    print(i.text)
    print(i['href'])
