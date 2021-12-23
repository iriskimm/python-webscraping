import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/list?titleId=675554'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

cartoons = soup.find_all('td', attrs={'class':'title'})

# title = cartoons[0].a.get_text()
# link = cartoons[0].a['href']
# print(title)
# print('http://comic.naver.com' + link)

# # 페이지에 있는 모든 웹툰 제목과 링크 구하기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = 'http://comic.naver.com' + cartoon.a['href']
#     print(title, link)

# 평점 구하기
total_rates = 0
ratings = soup.find_all('div', attrs={'class':'rating_type'})
for rating in ratings:
    rate = rating.strong.get_text() # OR
    # rate = rating.find('strong').get_text()
    print(rate)
    total_rates += float(rate)
print('Total rates:', total_rates)
print('Average rate:', (total_rates/len(cartoons)))
