from urllib.request import urlopen

# 获取网页html

url = 'http://www.baidu.com/'
response = urlopen(url)
# print(response.read().decode('latin1'))
with open("./1.html","w") as f:
    f.write(response.read().decode('utf-8'))
print('DONE')