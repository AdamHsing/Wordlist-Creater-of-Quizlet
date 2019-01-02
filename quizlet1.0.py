# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 19:53:19 2018

@author: Asus
"""
from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
    
    inputurl = input('请输入需要下载的quizlet链接：\n')
    inputname = input('请输入文件名称：\n')
    print('你的下载链接是：%s\n你的文件名称是：%s\n是否确认下载？（y\\n）\n' % (inputurl,inputname))
    Bool = input()
    if(Bool == 'y' or 'Y'):
        target = inputurl
        req = requests.get(url = target)
        html = req.text
        bf = BeautifulSoup(html, "lxml")
        texts = bf.find_all('span', class_="TermText notranslate lang-en")
        Len = len(texts)
        write_flag = True
        with open(inputname, 'a', encoding='utf-8') as f:
            f.write(inputname + '\n\n')
            for i in range(0,Len,2):
                f.writelines(str(texts[i].text))
                f.writelines(str('\n'))
                f.writelines(str(texts[(i+1)].text))
                f.writelines(str('\n\n'))
            f.write('\n\n')
    elif(Bool == 'n' or 'N'):
        exit()
