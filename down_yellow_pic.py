import requests
import webbrowser
from bs4 import BeautifulSoup
import os
import re 


def getHTMLText(url):    
    try:
        r = requests.get(url,timeout=30)
        print(r.url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('出现错误')
    
def getDownloadUrl(html,url_list):
    soup = BeautifulSoup(html,features='lxml')
    sub_list=soup.find_all('img',{"src": re.compile("http://www.+")})
    print(sub_list)

    for sub_tags in sub_list :
        #list_pic.append(sub_tags['src'])
        print(sub_tags)
        url_list.append(re.findall(r'http:.+"',str(sub_tags))[0][:-1])
    print(url_list)

def DownLoadPic(url_list):
    os.chdir('./img')
    for i in url_list:
        r = requests.get(i, stream=True)    # stream loading
        #file_name = i.split()
        print(i.split('/'))
        file_name = i.split('/')[-1]

        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('over')
    



def main():
    url_list=[]
    os.makedirs('./img/',exist_ok=True)
    url  = 'http://www.yeji556.com/picture/zipai/166723.html' 
    html = getHTMLText(url)#提取html源代码信息
    #提取源代码中的链接
    getDownloadUrl(html,url_list)
    DownLoadPic(url_list)
    
    
if __name__ == '__main__' :
    print('主函数开始执行爬取信息')
    main()
