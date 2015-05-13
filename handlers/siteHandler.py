#import lib.httpagentparser
import jinja2
import os
import logging
import urllib
import webapp2

from config import *
from lib import httpagentparser
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
    def error(self):
        mensaje='Mensaje de prueba'
        self.mi_error(mensaje)
    def exce(self):
        self.abort(500)

class ServiciosHandler(BaseHandler):
    def get(self):
        from webapp2 import Route
        template_val ={
        'metaDescripcion' : 'Consultorio general Gerardo Sepulveda',
        'metaKeyWords' : 'consultorio,gerardo,sepulveda',
        'metaCreador' : 'Erik Villegas'
        }
        self.render_template('index.html',**template_val)