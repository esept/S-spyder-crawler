import requests

# post 请求

url = 'https://fanyi.baidu.com/sug'
s = ''

data = {'kw':s}
resp = requests.post(url,data = data)
print(resp.json())

