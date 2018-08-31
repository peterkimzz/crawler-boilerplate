import pymysql.cursors

def setupMysql():

    conn = pymysql.connect(host='YOUR_HOST',
        user='YOUR_USER',
        password='YOUR_PASSWORD',
        db='YOUR_DATABASE')

    return conn