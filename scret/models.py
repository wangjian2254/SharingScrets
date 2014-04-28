#coding=utf-8
#Date: 11-12-8
#Time: 下午10:28

__author__ = u'王健'

from google.appengine.ext import db


class ScretUser(db.Model):
    nickname = db.StringProperty(indexed=False)


class Scret(db.Model):
    nickname = db.StringProperty(indexed=False)#作者
    title = db.StringProperty(indexed=False)#秘密标题
    content = db.TextProperty()#秘密内容
    updateTime = db.DateTimeProperty()#修改时间


class ScretGPS(db.Model):
    n = db.FloatProperty()#gps 经度
    s = db.FloatProperty()#gps 纬度

class ScretUp(db.Model):
    up = db.IntegerProperty()#顶次数

class ScretDown(db.Model):
    down = db.IntegerProperty()#踩次数

class ScretReplay(db.Model):
    updateTime = db.DateTimeProperty()#最后评论时间
    contentList = db.StringListProperty(indexed=False)#评论列表


