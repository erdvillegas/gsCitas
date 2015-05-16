#import lib.httpagentparser
import jinja2
import os
import logging
import urllib
import webapp2

from config import *
from lib import httpagentparser
from google.appengine.api import users
from handlers.BaseHandler import *
from webapp2_extras import jinja2
from webapp2_extras import json
from webapp2 import Router
from lib.ua_parser import *
from lib.user_agents import parse
from google.appengine.ext.webapp import template

 
class MainHandler(BaseHandler):
    def get(self):
        from webapp2 import Route
        template_val ={
        'metaDescripcion' : 'Consultorio general Gerardo Sepulveda',
        'metaKeyWords' : 'consultorio,gerardo,sepulveda',
        'metaCreador' : 'Erik Villegas'
        }
        self.render_template('index.html',**template_val)
    def login(self):
        self.render_template('login.html')


class ServiciosHandler(BaseHandler):
    def configMethod(self):
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))

        template_val ={
        'metaDescripcion' : 'Consultorio general Gerardo Sepulveda',
        'metaKeyWords' : 'consultorio,gerardo,sepulveda',
        'metaCreador' : 'Erik Villegas'
        }

        self.render_template("config.html",**template_val)