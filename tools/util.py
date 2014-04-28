#coding=utf-8
import re
import string
from jinja2 import filters
from jinja2.filters import environmentfilter

from setting import IsPassword

__author__ = 'wangjian2254'



def getResult(result,success=True,message=u'',status=200):
    return {'result':result,'success':success,'message':message,'status':status}


def datetimeformat(value, format='%Y-%m-%d %H:%M'):
    return value.strftime(format)


filters.FILTERS['datetimeformat'] = datetimeformat
