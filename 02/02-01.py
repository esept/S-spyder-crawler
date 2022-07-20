import re

text = "我的电话是:2124，你的电刷是:12312"
#
# lst = re.findall(r"\d+",text) # 返回列表
# iter = re.finditer(r'\d+',"我的电话是:2124，你的电刷是:12312")  # 返回迭代器
# print("1",lst,iter)
# for i in iter:
#     print(i)

# obj = re.compile("\d+") # 预加载re函数
#
# print(obj.match(text)) # 从句首开始匹配，如果句首没有符合的字符，则返回None，类似于"^\d+"
# print(obj.search(text)) # 从句首匹配到第一个符合的就返回
# obj.findall(text)
# obj.finditer(text)

'''
    在匹配自己
'''
f = open('./text','r')
text = f.read()
obj = re.compile(r"<a class=\"item-top item-1\" href=\"//(?P<urls>.*?)\"><h4>(?P<language>.*?)</h4>",re.S)
# 加上 re.S 则'.'可以匹配换行符
# (?P<group名称> 匹配的表达式 ) 可以将内容分组并命名，在.group("group名称")时使用
res = obj.finditer(text)
for i in res:
    print(i.group("urls"),end='->>')
    print(i.group("language"))