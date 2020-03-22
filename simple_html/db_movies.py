import requests
from bs4 import BeautifulSoup

# f = open('movies.txt','w', encoding='utf-8')
for i in range(10):
    url = 'https://movie.douban.com/top250?start='+str(i*25)+'&filter='
    # print(url)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    allmovies = soup.find_all('li')
    test = soup.find('h1')
    print(test)
    for movies in allmovies:
        print('fuck')
        rating = movies.find('em').text
        name = movies.find(class_='hd').find('span').text
        score = movies.find(class_='bd').find(class_='rating_num').text
        comment = movies.find(class_='inq').text
        href = movies.find(class_='hd').find('a')['href']
        print(rating+'----'+name+'---'+score+'---'+comment+'---'+href)
        # f.write()
# f.close()