from selenium import webdriver

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

    print('Selenium is ready to crawl.')
    
    return driver