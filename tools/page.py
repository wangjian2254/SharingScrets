#coding=utf-8
#
import json

__author__ = u'王健'
import os,webapp2,jinja2
from setting import TEMPLATE_DIR


class Page(webapp2.RequestHandler):
    def render(self, template_file, template_value):
        jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))
        template = jinja_environment.get_template(template_file)
        self.response.out.write(template.render(template_value))


    def flush(self,jsonobj):
        if isinstance(jsonobj,str):
            self.response.out.write(jsonobj)
        else:
            self.response.out.write(json.dumps(jsonobj))
