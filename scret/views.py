#coding=utf-8
#Date: 11-12-8
#Time: 下午10:28
from tools.page import Page

__author__ = u'王健'



class CreateScrets(Page):
    def get(self):
        username = self.request.get('username','')
        head = self.request.get('head','')
        appcode = self.request.get('appcode','')
        maxnum = self.request.get('maxnum',0)



    def post(self):
        self.get()

class UpdateScrets(Page):
    def get(self):
        username = self.request.get('username','')
        head = self.request.get('head','')
        appcode = self.request.get('appcode','')
        maxnum = self.request.get('maxnum',0)



    def post(self):
        self.get()


class GetScretsByUser(Page):
    def get(self):
        username = self.request.get('username','')
        head = self.request.get('head','')
        appcode = self.request.get('appcode','')
        maxnum = self.request.get('maxnum',0)



    def post(self):
        self.get()


class GetScretsByHot(Page):
    def get(self):
        username = self.request.get('username','')
        head = self.request.get('head','')
        appcode = self.request.get('appcode','')
        maxnum = self.request.get('maxnum',0)



    def post(self):
        self.get()


class GetScretsByReplay(Page):
    def get(self):
        username = self.request.get('username','')
        head = self.request.get('head','')
        appcode = self.request.get('appcode','')
        maxnum = self.request.get('maxnum',0)



    def post(self):
        self.get()


class GetReplayByScret(Page):
    def get(self):
        username = self.request.get('username','')
        head = self.request.get('head','')
        appcode = self.request.get('appcode','')
        maxnum = self.request.get('maxnum',0)



    def post(self):
        self.get()
