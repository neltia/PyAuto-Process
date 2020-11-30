import requests
from bs4 import BeautifulSoup

url = 'https://naver.com/' # 네이버 메인 페이지
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

# id가 NM_FAVORITE인 정보를 선택
data = soup.select('#NM_FAVORITE') # div.gnb_inner
print(data)