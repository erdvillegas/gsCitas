import lib.httpagentparser
import logging
import webapp2

from handlers.BaseHandler import *
from webapp2_extras import jinja2
from lib.ua_parser import *
from lib.user_agents import parse
from lib.google.appengine.ext.webapp import template


class SbAdmin(BaseHandler):
    """docstring for SbAdmin"webapp2.RequestHandler"""
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