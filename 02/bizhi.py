import requests
from bs4 import BeautifulSoup as bs
import time

url = 'https://www.umei.cc/bizhitupian/weimeibizhi/'
domaine = 'https://www.umei.cc'
path = ''
resp = requests.get(url)
resp.encoding = 'utf-8'
# print(resp.text)

main_page = bs(resp.text,"html.parser")
# print(main_page.find("ul",class_ = "pic-list after"))
alist = main_page.find("ul",class_ = "pic-list after").find_all("a") # <ul class="pic-list after">
i = 0
for a in alist:
    # print(a)
    # print(a.get("href"))
    img_page_resp = requests.get(domaine+a.get("href"))
    img_page_resp.encoding = 'utf-8'
    # print(img_page_resp.text)
    img_page_url = bs(img_page_resp.text,'html.parser')
    img_url = img_page_url.find("section",class_ = 'img-content').find('img')
    print(img_url.get("src"))
    img_res = requests.get(img_url.get("src"))
    img_name = img_url.get("src").split('/')[-1]
    time.sleep(1)
    # 保存图片的方式
    with open('imgs/'+img_name,mode='wb') as f:
        f.write(img_res.content)
    i += 1
    if i > 3:
        break
    
img_res.close()
    
    

