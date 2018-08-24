# -*- coding:utf-8 -*-
#爬虫

import urllib3
import urllib
import time
import base64
import requests
import os
from  bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

import re

driver = webdriver.Chrome()
driver.get("https://www.google.com/search?q=face&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiy-b_mwoTdAhWgwMQHHVgGBuoQ_AUICigB")

def scroll_foot(self):
    js = ""
    # 如何利用chrome驱动或phantomjs抓取
    if self.driver.name == "chrome" or self.driver.name == 'phantomjs':
        js = "var q=document.body.scrollTop=10000"
    # 如何利用IE驱动抓取
    elif self.driver.name == 'internet explorer':
        js = "var q=document.documentElement.scrollTop=10000"
    return self.driver.execute_script(js)

# url = "https://www.google.com/search?q=face&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiy-b_mwoTdAhWgwMQHHVgGBuoQ_AUICigB"

# headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
# req = urllib.request.Request(url=url, headers=headers)
# html = urllib.request.urlopen(req).read()
# soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
for i in range(10):
    driver.execute_script("var q=document.documentElement.scrollTop=" + str(i) + "0000")
    time.sleep(10)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
images = soup.findAll('img')
print(images)
imageName = 0
for i, image in enumerate(images):
    link = image.get('src')
    print(link)
    try:
        if link[0:4] == "data":
            code = link.replace('data:image/jpeg;base64,', '')
            code = code.encode('utf-8')
            imgdata = base64.b64decode(code)
            with open("D:/yc_projects/data/face_images/" + str(i) + '.bmp', 'wb') as w:
                w.write(imgdata)
            continue
        with open("D:/yc_projects/data/face_images/" + str(i) + '.bmp', 'wb') as w:
            w.write(requests.get(link).content)
    except:
        print("error")
