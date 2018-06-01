import pymysql


class Connect:

    conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       password='MySQL',
                       db='soporte_tp3')

    def openConnection(self):
        return self.conn

    def commit(self):
        self.conn.commit()

    def closeConnection(self):
        self.conn.close()
