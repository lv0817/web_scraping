import requests
import webbrowser

param = {'wd':'中北大学'}#搜索的信息
r = requests.get('https://www.baidu.com/s',params=param)
print(r.url)
webbrowser.open(r.url)