from bs4 import BeautifulSoup
from utils import mysql
import urllib.request
import json

def init():
    
    # MySQL
    conn = mysql.setupMysql()

    # List of Region
    region_list = ["busan", "chungbuk", "chungnam", "daegu", "daejun", "gwangju", "gyeonggi", "incheon", "jeju", "jeonbuk", "jeonnam", "kangwon", "kyungbuk", "kyungnam", "sejong", "seoul", "ulsan"]

    try:
        with conn.cursor() as cursor:
            sql = 'SELECT id, title, tel FROM academies WHERE address LIKE "%세종특별%" LIMIT 3'
            cursor.execute(sql)
            rows = cursor.fetchall()

            for row in rows:

                academy_tel = row[2]

                # DB에 전화번호가 있으면
                if len(academy_tel) > 0:

                    # 전화번호로 검색하고 
                    result = fetchPageUrl(academy_tel)
                # 없으면 API 호출을 하지 않는다.
                else:
                    print(f"{row[1]} doesn't have telephone numbebr in database.")

    finally:
        conn.close()


def fetchPageUrl(tel):

    # API keys
    client_id = "ZrNIqAaKLMG3vON4TC5f"
    client_secret = "oR39iWuuOr"

    search_keyword = urllib.parse.quote(tel)
    url = f"https://openapi.naver.com/v1/search/local?query={search_keyword}"
    # url = f"https://openapi.naver.com/v1/search/blog?query={search_keyword}"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    print(f'Search results for {tel}')
    if (rescode==200):

        response_body = response.read()
        response = response_body.decode('utf-8')
        response_json = json.loads(response)
        print(response_json.values())

        return response
    else:
        print("Error Code:" + rescode)
        return rescode

def extractAddress(address):
    address_list = address.split()

    if len(address_list) > 1:
        address = f'{address_list[0]} {address_list[1]}'
        return address

# run
init()
