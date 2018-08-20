import csv
from utils import mysql


def init():

    # mysql
    conn = mysql.setupMysql()

    # lists of region
    region_list = ["busan", "chungbuk", "chungnam", "daegu", "daejun", "gwangju", "gyeonggi", "incheon", "jeju", "jeonbuk", "jeonnam", "kangwon", "kyungbuk", "kyungnam", "sejong", "seoul", "ulsan"]

    # read csv
    for region in region_list:

        # file_path = f'/Users/rihankim/dev/crawl/region/listed/{region}_list.csv'
        file_path = f'/Users/rihankim/dev/crawl/region/listed/gyeonggi_list.csv'
        my_file = open(file_path, 'r', encoding='utf-8')

        academies = csv.reader(my_file)

        for i, academy in enumerate(academies):
            
            title = academy[0]
            field = academy[1]
            roadAddress = academy[2]
            tel = academy[4]
            teachingField = academy[5]
            teachingCourse = academy[6]
            teachingSubject = academy[7]

            try: 
                with conn.cursor() as cursor:
                    sql = 'INSERT INTO academies (title, field, roadAddress, tel, teachingField, teachingCourse, teachingSubject) VALUES (%s, %s, %s, %s, %s, %s, %s)'
                    cursor.execute(sql, (title, field, roadAddress, tel, teachingField, teachingCourse, teachingSubject))
                    conn.commit()
            finally:
                print(f"{title} is imported.")

# run
init()