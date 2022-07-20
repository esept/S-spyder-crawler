import re
import requests

# 从网页根据关键词下载png素材

url = 'https://www.pngpix.com/?q=' # png素材

keyword = 'computer'
path = '/'

myheader = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
}

res = requests.get(url+keyword,headers = myheader)

obj = re.compile(r'<a href=".*?" target="_blank"><img width=".*?" height=".*?" src="(?P<url>.*?.png)".*?',re.S)
urls = obj.findall(res.text)

for u in range(len(urls)):
    save_path = path+keyword+str(u)+'.png'
    # requests.get(urls[u]).content
    with open(save_path,'wb') as f:
        f.write(requests.get(urls[u]).content)
    
res.close()