import pymysql
class DBUtil:
    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="root",
            database="tpshop2.0",
            charset="utf8"
        )
    def query_one(self, sql):
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result

    def execute(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()
db_util = DBUtil()
