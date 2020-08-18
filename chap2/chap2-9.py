import requests
from bs4 import BeautifulSoup
import urllib


# Webページを取得して解析する
load_url = 'https://news.yahoo.co.jp/categories/it'
html = requests.get(load_url)
soup = BeautifulSoup(html.content, 'html.parser')

# すべてのタグを検索して、リンクを表示する
for element in soup.find_all("a"):
  print(element.text)
  url = element.get("href")
  link_url = urllib.parse.urljoin(load_url, url)
  print(link_url)