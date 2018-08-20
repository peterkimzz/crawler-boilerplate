import pymysql.cursors

def setupMysql():

    conn = pymysql.connect(host='rds-gangmom.cfl7dcbrw3yo.ap-northeast-2.rds.amazonaws.com',
        user='root',
        password='rkdskadjaak178',
        db='sandbox')

    return conn