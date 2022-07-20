import requests

'''
模拟浏览器登陆 - 处理cookie
防盗链处理
代理 - 防治被封ip
proxy = {
    "https" : "https:// /http:// /none ip adresse:port"
    "https":"https://218.60.8.83:3129"
}加入到resquest中
'''
# 会话
session = requests.session()
# session.get()
# session.post()
data = {
    "loginName" : "········",
    "password" : "·····"
}
# 登陆
url = ''
resp = session.post(url,data=data)
print(resp.text)
print(resp.cookies) # 查看cookie


# 如果使用resquests访问网页则需要
resp = requests.get(url,headers={
    "Cookie":"header···"
})
