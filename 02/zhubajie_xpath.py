from lxml import etree
import requests

url = 'https://www.zbj.com/search/service?kw=saas&r=1'
resp = requests.get(url)
# print(resp.text)

html = etree.HTML(resp.text) # etree 加载html
'''
//*[@id="__layout"]/div/div[3]/div/div[3]/div[4]/div[1]/div
//div[@class="search-result-list-service"]/div/a/div/div[1]/div
//*[@id="__layout"]/div/div[3]/div/div[3]/div[4]/div[1]/div/div[3]/a
//*[@id="__layout"]/div/div[3]/div/div[3]/div[4]/div[1]/div/div[3]/div/span
//*[@id="__layout"]/div/div[3]/div/div[3]/div[4]/div[1]/div/div[3]/div[2]
//*[@id="__layout"]/div/div[3]/div/div[3]/div[4]/div[1]/div/div[3]/div/div[@class="shop-info"]
'''
divs = html.xpath('//*[@id="__layout"]/div/div[3]/div/div[3]/div[4]/div[1]/div')
data = []
for div in divs:
    newlist = []
    newlist.append(div.xpath('./a/div/div[1]/div/text()')[0])
    newlist.append(div.xpath('./div[3]/a/text()')[0])
    newlist.append(div.xpath('./div[3]/div/div[@class="shop-info"]/text()')[0].strip('\n        '))
    newlist.append(div.xpath('./div[3]/div/span/text()')[0].strip("¥"))
    newlist.append("".join(div.xpath('./div[3]/div[2]/div/span/text()')))
    data.append(newlist)
    # print('\n')

resp.close()
for i in data:
    print(i)
# print(data)