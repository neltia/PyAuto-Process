import requests
from bs4 import BeautifulSoup

# 유저 설정
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}

# 네이버 메인이 아닌 DataLab 페이지
url = 'https://datalab.naver.com/keyword/realtimeList.naver?where=main'
res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.content, 'html.parser')

# span 태그의 이름이 item_title인 정보를 선택
data = soup.select('span.item_title')

# for 문으로 출력
for item in data:
    print(item.get_text())