import os

a=os.path

excel=a.dirname(a.dirname(a.realpath("cases.xlsx")))
live_path=a.join(excel,"new_1","CK_list","cases.xlsx")

conf=a.dirname(a.dirname(a.realpath("test.conf")))
conf_path=a.join(conf,"new_1","config")