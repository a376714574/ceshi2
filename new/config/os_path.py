import os

a=os.path

excel_old=a.dirname(a.dirname(a.realpath("cases.xlsx")))

excel_new=a.join(excel_old,"python15","new","ck_list","cases.xlsx")

print(excel_new)

config_old=a.dirname(a.dirname(a.realpath("config.conf")))

config_new=a.join(excel_old,"python15","new","config","config.conf")

print(config_new)