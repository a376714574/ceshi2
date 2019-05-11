from configparser import ConfigParser

from old.new_1 import excel
from old.new_1 import os_path


class conf:

    def __init__(self):
        a=ConfigParser()
        name=excel(os_path.live_path, "Switch").conf()
        a.read(os_path.conf_path + name, encoding="utf-8")
        self.Version=a.get("url_p","url")

    def version(self):
        return self.Version

