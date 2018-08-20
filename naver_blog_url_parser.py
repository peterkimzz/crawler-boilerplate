from bs4 import BeautifulSoup
from utils import mysql
import urllib.request

def init():
    conn = mysql.setupMysql()

    client_id = "ZrNIqAaKLMG3vON4TC5f"
    client_secret = "oR39iWuuOr"

    region_list = ["busan", "chungbuk", "chungnam", "daegu", "daejun", "gwangju", "gyeonggi", "incheon", "jeju", "jeonbuk", "jeonnam", "kangwon", "kyungbuk", "kyungnam", "sejong", "seoul", "ulsan"]

    business_name = '봄봄국어논술'
    search_keyword = urllib.parse.quote(business_name)
    url = f"https://openapi.naver.com/v1/search/local?query={search_keyword}"
    # url = f"https://openapi.naver.com/v1/search/blog?query={search_keyword}"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode==200):
        response_body = response.read()
        print(f"Search results for\n{business_name}")
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)

    # try: 
    #     with conn.cursor() as cursor:

          # sql = 'SELECT * FROM temp_academies WHERE address LIKE "%충청북도%"'
          # cursor.execute(sql)

          # rows = cursor.fetchall()

          # for index, row in enumerate(rows):
          #    row = rows[index]

          #    academy_id = row[0]
          #    title = row[1]
          #    address = row[2]
          #    tel = row[3]

          #    # tel is required field.
          #    if len(tel) > 0:

          #       search_keyword = urllib.parse.quote(tel)
          #       url = f"https://openapi.naver.com/v1/search/blog?query={search_keyword}"
          #       request = urllib.request.Request(url)
          #       request.add_header("X-Naver-Client-Id",client_id)
          #       request.add_header("X-Naver-Client-Secret",client_secret)
          #       response = urllib.request.urlopen(request)
          #       rescode = response.getcode()
          #       if(rescode==200):
          #           response_body = response.read()
          #           print(response_body.decode('utf-8'))
          #       else:
          #           print("Error Code:" + rescode)



           
    # finally:
    #   conn.close()

# run
init()
