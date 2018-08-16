# parser.py
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json
import os

# Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
driver = webdriver.Chrome('C://Users/root/dev/crawl/drivers/chromedriver.exe')
# PhantomJS의 경우 | 아까 받은 PhantomJS의 위치를 지정해준다.
# driver = webdriver.PhantomJS(
#     "C:\\Users\root\dev\crawl\phantomjs-2.1.1-windows\bin\phantomjs.exe")

# 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
driver.implicitly_wait(3)

# 크롬으로 url을 연다.
driver.get(
    'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')

# 엘리먼트 접근
driver.find_element_by_name('id').send_keys('NAVER_ID')
driver.find_element_by_name('pw').send_keys('NAVER_PASSWORD')
# 로그인 버튼을 눌러주자.
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

driver.get('https://order.pay.naver.com/home')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('div.p_inr > div.p_info > a > span')

for n in notices:
    print(n.text.strip())

# HTTP GET Request
# url = 'https://www.peterkimzz.com'
# req = requests.get(url)

# # python파일의 위치
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# # HTML 소스 가져오기
# html = req.text
# # HTTP Header 가져오기
# header = req.headers
# # HTTP Status 가져오기 (200: 정상)
# status = req.status_code
# # HTTP가 정상적으로 되었는지 (True/False)
# is_ok = req.ok

# soup = BeautifulSoup(html, 'html.parser')

# titles = soup.select(
#     'div.feed-container a div.wrapper div.contents h2.title')

# data = {}

# for title in titles:

#     print(title.text)

# for title in titles:
#     data[title.text] = title.get('href')

# with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
#     json.dump(data, json_file)
