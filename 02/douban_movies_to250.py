import re
import requests

myheader = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
}

url = 'https://movie.douban.com/top250?start='
for page in range(10):
    page_num = page*25
    print(page_num)
    res = requests.get(url+str(page_num),headers = myheader)
    print(res.request.url)

res.close()