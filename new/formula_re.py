from configparser import ConfigParser
import re
from new.mysql_rw import mysql

class formula_class:

    loan_id=None
    # def __init__(self):
    #     self.con = ConfigParser
    #     self.con.read("config/config.conf", encoding="utf-8")

    def formula_open(self):
        self.con=ConfigParser()
        self.con.read("config/config.conf",encoding="utf-8")

    def formula_intermediate(self,formula,data):
        print(formula)
        print(data)
        object=re.search(formula,data)

        obj_data=object.group(1)
        print(obj_data)

        conf_data=self.con.get("data", obj_data)
        print(conf_data)
        print(data)
        print(formula)
        print(type(conf_data))
        print(type(data))
        print(type(formula))

        if obj_data == "loan_id":
           my=mysql()
           my.mysql_connect(host="test.lemonban.com",user="test",password="test",port=3306)
           conf_data=my.mysql_sql(conf_data)
           print(conf_data)
           print(data)
           print(formula)
           print(type(conf_data))
           print(type(data))
           print(type(formula))
        return re.sub(formula,str(conf_data),data,count=1)

    def formula_clear(self):
        self.con.clear()