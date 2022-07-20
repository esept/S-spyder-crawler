import requests

header = {
    "User-Agent" :
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0"
}

url = "https://movie.douban.com/j/search_subjects?"
url2 = 'https://movie.douban.com/j/chart/top_list?'
param = {
    "type": "tv",
    "tag": "日剧",
    "sort": "recommend",
    "page_limit": 20,
    "page_start": 20
}
param2 = {
    "type": "19",
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20
}
resp = requests.get(url = url2 ,
                    headers = header ,
                    params = param2)

res = resp.json()
print(res)
res.close()


