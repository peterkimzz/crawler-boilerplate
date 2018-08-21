from utils import mysql
import json

def init():
    print('Mapping `tel` is started.')
    
    conn = mysql.setupMysql()
  
    with conn.cursor() as cursor:
        sql = " id, title, tel, roadAddress FROM academies LIMIT 3"
        cursor.execute(sql)
        rows = cursor.fetchall()
        print(rows)









# run
init()