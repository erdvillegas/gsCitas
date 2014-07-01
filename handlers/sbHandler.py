import lib.httpagentparser
import jinja2
import os
import logging
import urllib
import webapp2

from handlers.BaseHandler import *
from config import *
from webapp2_extras import jinja2
from webapp2 import Router
from lib.ua_parser import *
from lib.user_agents import parse
from lib.google.appengine.ext.webapp import template


class SbAdmin(BaseHandler):
    """docstring for SbAdmin"webapp2.RequestHandler"""
    def get(self):
        from webapp2 import Route
        self.render_template('index.html')
    def blank(self):
        self.render_template('blank.html')
    def buttonts(self):
        self.render_template('buttons.html')
    def flot(self):
        self.render_template('flot.html')
    def forms(self):
        self.render_template('forms.html')
    def grid(self):
        self.render_template('grid.html')
    def login(self):
        self.render_template('login.html')
    def morris(self):
        self.render_template('morris.html')
    def notifications(self):
        self.render_template('notifications.html')
    def panels(self):
        self.render_template('panels-wells')
    def tables(self):
        self.render_template('tables.html')
    def typography(self):
        self.render_template('typography.html')
    def error(self):
        mensaje='Mensaje de prueba'
        self.mi_error(mensaje)
    def exce(self):
        self.abort(500)