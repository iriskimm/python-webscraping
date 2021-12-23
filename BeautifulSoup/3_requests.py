import requests

res = requests.get('http://google.com')  # res stands for response
res.raise_for_status()

# print('Response code:', res.status_code) # to check if it's working; 200이면 정상


# if res.status_code == requests.codes.ok: # 200 means it's ok
#     print('정상입니다')
# else:
#     print('문제가 생겼습니다. [에러코드', res.status_code, ']')


# print(res) # prints out <Response [200]>
# print(res.text) # prints out the html

print(len(res.text))
print(res.text)

with open('mygoogle.html', 'w', encoding='utf8') as f:
    f.write(res.text)
