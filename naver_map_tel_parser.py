import csv
from bs4 import BeautifulSoup
from selenium import webdriver
import pymysql.cursors


def init():
    # selemium
    driver = getDriver()

    # mysql
    conn = setupMysql()

    region_list = ['kyungnam_nonum', 'seoul_nonum', 'ulsan_nonum']

    # file_path = '/Users/rihankim/dev/crawl/region/nonum/chungnam_nonum.csv'
    url = 'https://map.naver.com'

    # read csv
    for region in region_list:

        print(f'Searching tel-number is started at {region}.')
        file_path = f'/Users/rihankim/dev/crawl/region/nonum/{region}.csv'
        my_file = open(file_path, 'r', encoding='utf-8')

        academies = csv.reader(my_file)

        for i, academy in enumerate(academies):
            
            title = academy[0]
            address_list = academy[2]

            address = extractAddress(address_list)
            search_keyword = f'{address} {title}'

            # open browser
            driver.get(url)
            driver.find_element_by_id('search-input').send_keys(search_keyword)
            btn = driver.find_element_by_css_selector('div.sch fieldset button')
            btn.click()

            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            cards = soup.select('div.lsnx dl.lsnx_det')
            tels = soup.select('div.lsnx dl.lsnx_det dd.tel')

            if len(cards) < 1:
                print(f"Can't find {title} on Naver Maps.")
            else:
                
                if len(tels) < 1:
                    print(f"{title} has not registered on Naver Maps.")
                else:
                    tel = tels[0].text.strip()
                    print(f'{title} {tel}')
                    try: 
                        with conn.cursor() as cursor:
                            sql = 'INSERT INTO academies (title, address, tel) VALUES (%s, %s, %s)'
                            cursor.execute(sql, (title, address_list, tel))
                            conn.commit()
                    finally:
                        a = 1

    print('Finished finding telephone number of academy.')


def setupMysql():

    conn = pymysql.connect(host='rds-gangmom.cfl7dcbrw3yo.ap-northeast-2.rds.amazonaws.com',
        user='root',
        password='rkdskadjaak178',
        db='sandbox')
    
    return conn


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
        '/Users/rihankim/dev/crawl/libs/chromedriver', options=options)
    driver.implicitly_wait(3)
    return driver


def extractAddress(address):
    address_list = address.split()

    if len(address_list) > 1:
        address = f'{address_list[0]} {address_list[1]}'
        return address

# run
init()