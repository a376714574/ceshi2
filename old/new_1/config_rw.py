import re
from configparser import ConfigParser

from old.new_1 import os_path


class formula_re:

    def re_start(self,name):
        self.config=ConfigParser()
        print(os_path.conf_path)
        print(name)
        self.config.read(R"C:\Users\Administrator\PycharmProjects\python_15\new_1\config\OL.conf",encoding="utf-8")

    def replace(self,formula,data):

        match_object=re.search(formula, data)

        data_1=match_object.group(1)

        con_gdata=self.config.get("data",data_1)

        return re.sub(formula, con_gdata, data, count=1)

    def re_clear(self):
        self.config.clear()
