import pymysql

class mysql:

    def mysql_connect(self,host,user,password,port):
        print(host,user,password,port,"1111111111111111111111111111111111111")
        self.my_connect=pymysql.connect(host=host,user=user,password=password,port=port)
        self.Console=self.my_connect.cursor()
        print(self.Console)

    def mysql_sql(self,sql):
        print(sql)
        print(type(sql))
        if sql == "config":
            print(self.Console)
            self.Console.execute(sql)
            result=self.Console.fetchone()
            print(result)
        else:
            print(sql,"-----------------------111")
            self.Console.execute(sql)
            print(self.Console.execute(sql))
            result=self.Console.fetchone()
            print(result)
            print(result[0])
            result=result[0]
        return result

    def mysql_clear(self):
        self.my_connect.close()