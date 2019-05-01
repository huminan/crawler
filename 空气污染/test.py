# coding=utf-8
import json
import requests
import re
from selenium import webdriver

url = 'http://aqicn.org/map/cn/'
chrome_path = 'C:\Program Files\chromedriver.exe'
browser = webdriver.Chrome(executable_path = chrome_path)
browser.get(url)

url = 'https://api.waqi.info/mapq/bounds/'
# 地图的边界, 
para = {'bounds':'0.7031073524364909,61.08398437500001,48.22467264956519,155.91796875000003', 'inc':'placeholders'}

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}
req = requests.Session()
cookies = browser.get_cookies()
for cookie in cookies:
    req.cookies.set(cookie['name'], cookie['value'])
r=req.get(url, headers=headers, params=para)
if r.status_code == 200:    # Request 成功!
    for dict in r.json():
        city = re.search('\((.*)\)', dict['city'])
        if city is None:
            print('Unkown Chinese city name!')
        else:
            print(city.group(1) + '的空气污染指数为: ' + dict['aqi'])
else:
    print(r.status_code)
file_name = './空气污染.json'
with open(file_name, 'w') as file_obj:
    json.dump(r.json(), file_obj)
''' #民生银行
url = 'https://nper.cmbc.com.cn/pweb/static/login.html'
chrome_path = 'C:\Program Files\chromedriver.exe'
browser = webdriver.Chrome(executable_path = chrome_path)
browser.get(url)
# 输入账号
input = browser.find_element_by_id('writeUserId')
input.send_keys("123456789")
# 输入密码
input = browser.find_element_by_id('cLoginPassWord')
input.send_keys("123456789")
# 点击登陆
browser.find_element_by_id('loginButton').submit()
'''