import os
import jinja2
import webapp2
import logging
from webapp2 import Router


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Hello World")
    def myMethod(self,user):
        self.response.write("Hola " + user)