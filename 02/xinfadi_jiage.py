import requests
from bs4 import BeautifulSoup
import re
import csv
url = 'http://www.xinfadi.com.cn/getPriceData.html'
myheader = {
    "User-Agent" :"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0"
}
dict = {
    "limit": 40,
    "current": 1,
    "pubDateStartTime": '',
    "pubDateEndTime": '',
    "prodPcatid": '',
    "prodCatid": '',
    "prodName": ''
}

'''
{"id":1301692,"prodName":"大白菜","prodCatid":1186,"prodCat":"蔬菜","prodPcatid":null,"prodPcat":"","lowPrice":"0.5","highPrice":"0.7","avgPrice":"0.6","place":"冀","specInfo":"","unitInfo":"斤","pubDate":"2022-07-05 00:00:00","status":null,"userIdCreate":138,"userIdModified":null,"userCreate":"admin","userModified":null,"gmtCreate":null,"gmtModified":null}
'''

domaine = requests.post(url,headers = myheader,data=dict)

obj = re.compile(r'{"id":.*?,"prodName":"(?P<name>.*?)",.*?"lowPrice":"(?P<low_p>.*?)","highPrice":"(?P<high_p>.*?)".*?"place":"(?P<place>.*?)".*?}')
res = obj.finditer(domaine.text)
# f = open("priceofveg.csv","w")
# csvwriter = csv.writer(f)

for i in res:
    print(i.group("name"),i.group("low_p"),i.group("high_p"),i.group("place"))
    # csvwriter.writerow([i.group("name"),i.group("low_p"),i.group("high_p")])


# f.close()