''' 防盗链处理
梨视频
源代码中没有<video>标签
视频主页面 ： https://www.pearvideo.com/video_1767099
检查显示视频地址（可播放）：https://video.pearvideo.com/mp4/third/20220708/cont-1767099-10305425-001242-hd.mp4
XHR中查找视频地址（不可播放）：https://video.pearvideo.com/mp4/third/20220708/1657267723007-10305425-001242-hd.mp4
需要将 cont-1767099 替换到 1657267723007 的位置
'''

import requests

url = 'https://www.pearvideo.com/video_1767099'
videostatus = 'https://www.pearvideo.com/videoStatus.jsp?contId=1767099&mrd=0.2410393585672852'


myheader = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "Referer": url # 防盗链
}

resp = requests.get(videostatus,headers = myheader) #@this_is_a_test
video_resp = resp.json()
# print(video_resp)

video_1_url = video_resp["videoInfo"]["videos"]["srcUrl"]
replaceID = video_resp["systemTime"]
contID = url.split("_")[1]
video_2_url = video_1_url.replace(replaceID,"cont-"+contID)
# print(video_1_url,replaceID,contID)
print(video_2_url)
with open('./lishipin.mp4','wb') as f:
    f.write(requests.get(video_2_url).content)
resp.close()

