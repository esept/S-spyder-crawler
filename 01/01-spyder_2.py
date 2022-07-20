import requests

# get请求

query = 'chinese mnist'
url = f'https://m.sogou.com/web/searchList.jsp?dp=1&keyword={query}'
myheader = {"User-Agent" :"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0"}
res = requests.get(url,headers = myheader)
print(res)
print(res.text)