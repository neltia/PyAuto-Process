# Crawling Library
import requests
import pandas as pd
import datetime
from bs4 import BeautifulSoup
import re
from datetime import datetime

# define data
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
main_url = 'https://www.boannews.com'
accident_url = main_url + '/search/news_total.asp?search=key_word&find=%BB%E7%B0%C7%BB%E7%B0%ED'

# define function
def clean_date(string):
  p = re.compile('\d{4}-\d{2}-\d{2} \d{1,2}:\d{1,2}')
  data = p.search(string).group()
  date_value = datetime.strptime(data, "%Y-%m-%d %H:%M")
  return date_value

def get_src(tag_list):
  img_list = []
  for index in tag_list:
    tag = index.find_all('img')
    for img in tag:
      img_list.append(img.get('src'))
  return img_list

# get url list
res = requests.get(accident_url, headers=headers)
soup = BeautifulSoup(res.content, 'html.parser')
news_list = soup.find_all("div", {"class":"news_list"})
url_list = [index.find('a').get('href').split('&')[0] for index in news_list]

# getting news data
date = []
title = []
contents = []
photos = []

for index in url_list:
	url = main_url + index
	res = requests.get(url, headers=headers)
	soup = BeautifulSoup(res.content, 'html.parser')

	title.append(soup.find("div", {"id":"news_title02"}).text)
	contents.append(soup.find("div", {"id":"news_content"}).text.strip())
	date.append(soup.find("div", {"id":"news_util01"}).text.strip())
	photos.append(soup.find_all("div", {"class":"news_image"}))

# preprocess
df_data = {}
df_data["date"] = date
df_data["title"] = title
df_data["contents"] = contents
df_data["photos"] = photos
df_data["url"] = url_list
df = pd.DataFrame(df_data)

df["date"] = [clean_date(data) for data in df["date"]]
df["photos"] = [get_src(data) for data in df["photos"]]
print(df)

"""

print(title)
print(contents)
print(date)
print(photos)
"""