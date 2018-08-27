from bs4 import BeautifulSoup
from utils import mysql
import urllib.request
import json
import time

# MySQL
conn = mysql.setupMysql()

def init():

    # List of Region
    region_list = ["busan", "chungbuk", "chungnam", "daegu", "daejun", "gwangju", "gyeonggi", "incheon", "jeju", "jeonbuk", "jeonnam", "kangwon", "kyungbuk", "kyungnam", "sejong", "seoul", "ulsan"]

    try:
        with conn.cursor() as cursor:
            sql = """
            SELECT 
                id, 
                title, 
                tel 
            FROM 
                leads 
            WHERE 
                tel > "" AND
                isUrlParsed != 1
            """
            cursor.execute(sql)
            rows = cursor.fetchall()

            for row in rows:

                academy_id = row[0]
                academy_tel = row[2]

                if len(academy_tel) > 0:
                    time.sleep(0.2)
                    fetchPageUrl(academy_id, academy_tel)
                else:
                    print(f'{academy_id} dosen not have a tel-number.')

    finally:
        conn.close()
        print('Parsing Blog Url is finished.')


def fetchPageUrl(id, tel):

    # API keys
    client_id = "ZrNIqAaKLMG3vON4TC5f"
    client_secret = "oR39iWuuOr"

    search_keyword = urllib.parse.quote(tel)
    url = f"https://openapi.naver.com/v1/search/local?query={search_keyword}"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode==200):
        response_body = response.read()
        response = response_body.decode('utf-8')
        response_json = json.loads(response)
        items = response_json['items']
        
        # 검색 결과가 있을 때
        if len(items) > 0:
            item = items[0]
            link = item['link']

            # link가 있을 때
            if len(link) > 0:

                with conn.cursor() as cursor:
                    sql = f"""
                    UPDATE
                        leads
                    SET
                        link = "{link}",
                        isUrlParsed = 1
                    WHERE
                        id = {id}
                    """
                    print(f'{id} {tel} -> {link} is updated.')
                    result = cursor.execute(sql)
                    conn.commit()
            # link가 없을 때
            else:
                with conn.cursor() as cursor:
                    sql = f"""
                    UPDATE
                        leads
                    SET
                        isUrlParsed = 1
                    WHERE
                        id = {id}
                    """
                    print(f'{id} {tel} does not have a link.')
                    result = cursor.execute(sql)
                    conn.commit()
        # 검색 결과가 없을 때
        else:
            with conn.cursor() as cursor:
                    sql = f"""
                    UPDATE
                        leads
                    SET
                        isUrlParsed = 1
                    WHERE
                        id = {id}
                    """
                    print(f'{id} {tel} does not have any result.')
                    result = cursor.execute(sql)
                    conn.commit()
    else:
        print("Error Code:" + rescode)

def extractAddress(address):
    address_list = address.split()

    if len(address_list) > 1:
        address = f'{address_list[0]} {address_list[1]}'
        return address

# run 3 times each a minute.
init()
sleep(20)
init()
sleep(20)
init()