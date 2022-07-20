import requests
import re
import csv
from concurrent.futures import ThreadPoolExecutor

domain = 'http://www.xinfadi.com.cn/getPriceData.html'
myheader = {
    # "Referer":" http://www.xinfadi.com.cn/priceDetail.html",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
}





def get_one_page_data(num):
    dict = {
        "limit": "20",
        "current": num,
    }
    resp = requests.post(url=domain,data=dict,headers = myheader)
    text = resp.text
    # print(text)
    obj = re.compile(r'{"id":.*?,"prodName":"(?P<name>.*?)",.*?"lowPrice":"(?P<low_p>.*?)","highPrice":"(?P<high_p>.*?)".*?"place":"(?P<place>.*?)".*?}')
    res = obj.finditer(text)
    # print(resp.request.url)
    for i in res:
        # print(i.group("name"),i.group("low_p"),i.group("high_p"),i.group("place"))
        csvwriter.writerow([i.group("name"),i.group("low_p"),i.group("high_p"),i.group("place")])
    resp.close()

if __name__ == '__main__':
    f = open("xinfadi_99pages.csv", "w")
    csvwriter = csv.writer(f)
    with ThreadPoolExecutor(50) as t:
        for i in range(1,100):
            t.submit(get_one_page_data(i))
            print(i)
    f.close()
    print("DONE")

