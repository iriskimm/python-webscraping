import requests

# url 에 접속이 허용되지 않을때 user agent를 사용하여 접속을 가능케 함

url = 'http://nadocoding.tistory.com'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

res = requests.get(url, headers=headers) # res stands for response
res.raise_for_status()

with open('nadocoding.html', 'w', encoding='utf8') as f:
    f.write(res.text)