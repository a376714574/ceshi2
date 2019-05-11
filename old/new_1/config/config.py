from configparser import ConfigParser

from old.new_1 import excel
from old.new_1 import os_path


class conf:

    def __init__(self):
        a=ConfigParser()
        name=excel(os_path.live_path, "Switch").conf()
        print(os_path.live_path)
        print(os_path.conf_path)
        print(name)
        a.read(r"C:\Users\Administrator\PycharmProjects\python_15\new_1\config\OL.conf",encoding="utf-8")


        self.Version=a.get("url_p","url")

    def version(self):
        return self.Version

