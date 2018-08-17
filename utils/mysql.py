import pymysql.cursors

def setupMysql():

    conn = pymysql.connect(host='localhost',
        user='root',
        password='qkfhrkrl0412',
        db='gangmom')

    return conn