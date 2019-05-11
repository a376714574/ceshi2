import requests

from old.new_1 import conf


class get_post:

    def __init__(self):
        self.url_p=conf().version()

    def sess_open(self):
        self.sess=requests.sessions.session()

    def req_gp(self,mode,url,data):

        url_1=self.url_p+url
        if mode=="get":
            print(mode)
            print(url_1)
            print(type(data))
            req=self.sess.request(method=mode,url=url_1,params=eval(data))
        elif mode=="post":
            print(mode)
            print(url_1)
            print(data)
            req=self.sess.request(method=mode,url=url_1,data=eval(data))
        else:
            print("不支持")
        print(req.text)
        print("12")
        return req.text

    def sess_close(self):
        self.sess.close()

