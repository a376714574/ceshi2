import pymysql

class mysql:

    def connect(self):
        self.my_connect = pymysql.connect(host="test.lemonban.com", user="test", password="test", port=3306)
        self.sql_input=self.my_connect.cursor()

    def sql_action(self,sql):
        self.sql_input.execute(sql)
        return self.sql_input.fetchone()

    def mysql_close(self):
        self.sql_input.close()
        self.my_connect.close()