import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

# get all categories
categories_list = soup.find(class_='side_categories').find(class_='nav nav-list')
categories = categories_list.find('ul').find_all('li')
for item in categories:
    print(item.text)

print('----------------------')
url2 = 'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
res2 = requests.get(url2)
soup2 = BeautifulSoup(res2.text, 'html.parser')

# get the name,star,price
f = open('books.txt','w', encoding ="utf-8")

items = soup2.find_all(class_='product_pod')
for item in items:
    name = item.find('h3').find('a')['title']
    star = item.find('p')['class']
    price = item.find(class_='product_price').find('p', class_='price_color')
    print('name: ' + name + ' star-rating: ' + star[1] + ' price: ' + price.text)
    f.write('name: ' + name + '--- star-rating: ' + star[1] + ' --- price: ' + price.text + '\n')

f.close()