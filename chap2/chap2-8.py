import requests
from bs4 import BeautifulSoup


# Webページを取得して解析する
load_url = 'https://news.yahoo.co.jp/categories/it'
html = requests.get(load_url)
soup = BeautifulSoup(html.content, 'html.parser')

# すべてのタグを検索して、リンクを表示する
for element in soup.find_all("a"):
  print(element.text)
  url = element.get("href")
  print(url)