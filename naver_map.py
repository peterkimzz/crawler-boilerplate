import csv
from bs4 import BeautifulSoup
from selenium import webdriver

my_file = open('C://Users/root/dev/crawl/region/nonum/chungbuk_nonum.csv')
rdr = csv.reader(my_file, 'r', encoding='utf-8')

for line in rdr:
    print(line)
my_file.close()

# # configure selenium options
# options = webdriver.ChromeOptions()
# # hedless
# options.add_argument('headless')
# # for responsive web
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")
# # force change user-agent of selenium
# options.add_argument(
#     "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
# # korean language
# options.add_argument("lang=ko_KR")

# driver = webdriver.Chrome(
#     'C://Users/root/dev/crawl/drivers/chromedriver.exe', chrome_options=options)
# driver.implicitly_wait(3)

# url = 'https://map.naver.com'
# search_keyword = '부산광역시 사하구 세종프라임학원'

# driver.get(url)
# driver.find_element_by_id('search-input').send_keys(search_keyword)
# btn = driver.find_element_by_css_selector('div.sch fieldset button')
# btn.click()

# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# tels = soup.select('div.lsnx dl.lsnx_det dd.tel')

# for tel in tels:
#     print(tel.text)

# driver.quit()
