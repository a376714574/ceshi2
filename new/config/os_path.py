import os

a=os.path

excel_old=a.dirname(a.dirname(a.realpath("cases.xlsx")))

excel_new=a.join(excel_old,"new","ck_list","cases.xlsx")


config_old=a.dirname(a.dirname(a.realpath("config.conf")))

config_new=a.join(excel_old,"new","config","config.conf")

