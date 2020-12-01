import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}

main_url = 'https://www.boannews.com/search/news_total.asp?search=key_word&find=%BB%E7%B0%C7%BB%E7%B0%ED'
res = requests.get(main_url, headers=headers)
soup = BeautifulSoup(res.content, 'html.parser')

url = 'https://www.boannews.com' + soup.find(class_='news_list').find('a').get('href')
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.content, 'html.parser')

title = soup.find("div", {"id":"news_title02"}).text
contents = soup.find("div", {"id":"news_content"}).text
date = soup.find("div", {"id":"news_util01"}).text.strip()
photos = soup.find_all("div", {"clas":"news_image"})

print(title)
print(contents)
print(date)
print(photos)
