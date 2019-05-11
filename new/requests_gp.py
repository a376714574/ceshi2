import requests
from requests import request
from configparser import ConfigParser
import json

class Req_PG:

    def __init__(self):
        con = ConfigParser()
        con.read("config/config.conf", encoding="utf-8")
        self.url_p=con.get("url_p", "url")

    def req_open(self):
        self.sess = requests.sessions.session()
        self.cookies=self.sess.cookies
        print(self.cookies)
    def req_pg(self,mode,url,data):

        url=self.url_p+url

        if mode=="post":
            print(self.cookies)
            print(data)
            # print(type(json.loads(data)))
            print(mode)
            print(url)
            req=self.sess.request(method=mode,data=eval(data),url=url,cookies=self.cookies)

        elif mode=="get":
            req=self.sess.request(method=mode,params=eval(data),url=url)

        return req

    def req_close(self):
        self.sess.close()


