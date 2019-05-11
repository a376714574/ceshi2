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
           req=(self.sess.request(mode,url_1,data)).text
        elif mode=="post":
            req=self.sess.request(method=mode,url=url_1,data=eval(data))
        else:
            print("不支持")

        return str(req.text)

    def sess_close(self):
        self.sess.close()