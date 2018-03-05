from bs4 import BeautifulSoup
import urllib.request
import re
import random

base_url = 'https://baike.baidu.com'
his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]


for i in range(20):
    url = base_url+his[-1]
    html = urllib.request.urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html,features='lxml')
    print(i,soup.find('h1').get_text(),' url',his[-1])#h1是主标题

    # find valid urls
   #下面的语句有两种方法
   #sub_urls = soup.find_all("a",{ "target":"_blank", "href": re.compile("/item/(%.{2})+$")})
    sub_urls = soup.find_all("a",\
    target="_blank", href=re.compile("/item/(%.{2})+$"),limit=10)
    if len(sub_urls)!=0:
        his.append(random.sample(sub_urls,1)[0]['href'])
        
    else:
        his.pop()
print(his)