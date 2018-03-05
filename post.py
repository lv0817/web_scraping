import requests
import webbrowser

data = {'menhuusername':'lvjiawei17@mails.ucas.ac.cn','menhupassword':'lv0817'}

r = requests.post('http://sep.ucas.ac.cn/getTaskTip',data=data)
print(r.text)
print(r.cookies.get_dict())

