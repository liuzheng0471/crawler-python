import requests
from bs4 import BeautifulSoup

url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/'
res = requests.get(url)
html = res.text
soup = BeautifulSoup(html, 'html.parser')

comment_list = soup.find(class_='comment-list')

comments = comment_list.find_all(class_='comment-content')

for comment in comments:
    print(comment.text)

url2 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/'
res2 = requests.get(url2)
soup2 = BeautifulSoup(res2.text, 'html.parser')

articles = soup2.find_all(class_='entry-header')
for article in articles:
    name = article.find(class_='entry-title').find('a')
    time = article.find('time')['datetime']
    href = name['href']
    print(time)
    print(name.text)
    print(href)
    print('-----------')