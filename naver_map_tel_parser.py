import csv
from bs4 import BeautifulSoup
from selenium import webdriver


def init():
    driver = getDriver()
    file_path = 'C://Users/root/dev/crawl/region/nonum/chungbuk_nonum.csv'
    url = 'https://map.naver.com'
    my_file = open(file_path, encoding='utf-8')
    academies = csv.reader(my_file)

    for academy in academies:

        title = academy[0]
        address_list = academy[2]

        address = extractAddress(address_list)
        search_keyword = f'{address} {title}'

        driver.get(url)
        driver.find_element_by_id('search-input').send_keys(search_keyword)
        btn = driver.find_element_by_css_selector('div.sch fieldset button')
        btn.click()

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        cards = soup.select('div.lsnx dl.lsnx_det')
        tels = soup.select('div.lsnx dl.lsnx_det dd.tel')

        print(cards)

        # for tel in tels:
        #     print(tel)

        #     if len(tel.text) > 0:
        #         print(tel.text)

    driver.quit()
    print('Finished finding telephone number of academy.')


def getDriver():
    # configure selenium options
    options = webdriver.ChromeOptions()
    # hedless
    options.add_argument('headless')
    # for responsive web
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    # force change user-agent of selenium
    options.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
    # korean language
    options.add_argument("lang=ko_KR")

    driver = webdriver.Chrome(
        'C://Users/root/dev/crawl/drivers/chromedriver.exe', chrome_options=options)
    driver.implicitly_wait(3)
    return driver


def extractAddress(address):
    address_list = address.split()

    if len(address_list) > 1:
        address = f'{address_list[0]} {address_list[1]}'
        return address


init()
