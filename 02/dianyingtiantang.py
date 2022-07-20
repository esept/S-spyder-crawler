import re
import requests
from bs4 import BeautifulSoup as bs
import csv

# 电影天堂的2022必看热片-> 电影名称 + 下载链接

domain = 'https://www.dy2018.com'
res = requests.get(domain)
res.encoding = 'gbk'


page = bs(res.text,"html.parser") # 生成bs对象
table = page.find("div",class_ = "co_area2",style = "float:left;width:470px;height:auto;overflow:hidden;margin-left:6px;")
# class 是python关键字,因此需要在后面加上_
# 或者使用
# table = page.find(“table”,attrs={“class”:”hq_table”}) <li><a href=".*?" .*?</font></span></li>
obj = re.compile(r'<li><a href="(?P<url>.*?)" .*?</a><span><font color="#FF0000">.*?</font></span></li>',re.S)
urls = obj.finditer(str(table))
# print(urls)

f = open("name.csv","w")
csvwriter = csv.writer(f)
# csvwriter = writerrow([…])

for url in urls:
    # print(url.group("url"))
    movie_page = requests.get(domain+url.group("url"))
    print(movie_page.request.url)
    # movie_obj = re.compile(r'<br />◎片\u3000\u3000名\u3000(?P<movie_name>.*?)<br />',re.S)

    movie_obj = re.compile('<br />◎片\u3000\u3000名\u3000(?P<movie_name>.*?)<br />.*?<a href="(?P<movie_url>magnet:.*?)">.*?</a>',re.S)
    movie_res = movie_obj.findall(movie_page.content.decode('gbk'))
    
    print(movie_res)
    csvwriter.writerow(movie_res)

f.close()
res.close()
movie_page.close()
# requests.close()