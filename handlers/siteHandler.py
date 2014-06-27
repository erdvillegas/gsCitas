import os
import webapp2
import logging
from webapp2 import Router
from webapp2_extras import routes
import httpagentparser
from ua_parser import *
from user_agents import parse
from config import *
from google.appengine.ext.webapp import template
from webapp2 import Route

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_val = {
        'staticF' : STATIC_FILES,
        'title' : 'gsCitas',
        'projectName' : 'Gerardo Sepulveda, Citas',
        }
        path = os.path.join(TEMPLATE_PATH, 'index.html')
        self.response.out.write(template.render(path, template_val))
        #self.response.write("Hello World")
    def myMethod(self,user):
        self.response.write("Hola " + user)
    def ruta(self):
    	self.response.write(self.request.application_url)
    def agente(self):
    	agente = self.request.headers.get('User-Agent')
    	self.response.write(agente)
    def device(self):
        agente = self.request.headers.get('User-Agent')
        device = httpagentparser.simple_detect(agente)
        self.response.write(device)
    def opsi(self):
    	agente = self.request.headers.get('User-Agent')
    	device = httpagentparser.detect(agente)
    	ua_string = agente
    	user_agent = parse(ua_string)
    	self.response.write(user_agent.os.family)

class SbAdmin(webapp2.RequestHandler):
    """docstring for SbAdmin"webapp2.RequestHandler"""
    def get(self):
        template_val = {
        'static' : STATIC_FILES
        }
        from webapp2 import Route
        path = os.path.join(TEMPLATE_PATH, 'index.html')
        self.response.out.write(template.render(path, template_val))
    def blank(self):
        template_val = {
        'static' : STATIC_FILES
        }
        path = os.path.join(TEMPLATE_PATH, 'blank.html')
        self.response.out.write(template.render(path, template_val))
    def buttonts(self):
        template_val = {
        'static' : STATIC_FILES
        }
        path = os.path.join(TEMPLATE_PATH, 'buttons.html')
        self.response.out.write(template.render(path, template_val))
    def flot(self):
        template_val = {
        'static' : STATIC_FILES
        }
        path = os.path.join(TEMPLATE_PATH, 'flot.html')
        self.response.out.write(template.render(path, template_val))
    def forms(self):
        template_val = {
        'static' : STATIC_FILES
        }
        path = os.path.join(TEMPLATE_PATH, 'forms.html')
        self.response.out.write(template.render(path, template_val))
    def grid(self):
        template_val = {
        'static' : STATIC_FILES
        }
        path = os.path.join(TEMPLATE_PATH, 'grid.html')
        self.response.out.write(template.render(path, template_val))
    def login(self):
        template_val = {
        'static' : STATIC_FILES
        }
        path = os.path.join(TEMPLATE_PATH, 'login.html')
        self.response.out.write(template.render(path, template_val))
    def morris(self):
        template_val = {
        'static' : STATIC_FILES
        }
        path = os.path.join(TEMPLATE_PATH, 'morris.html')
        self.response.out.write(template.render(path, template_val))
    def notifications(self):
        template_val = {
        'static' : STATIC_FILES
        }
        path = os.path.join(TEMPLATE_PATH, 'notifications.html')
        self.response.out.write(template.render(path, template_val))
    def panels(self):
        template_val = {
        'static' : STATIC_FILES
        }
        path = os.path.join(TEMPLATE_PATH, 'panels-wells.html')
        self.response.out.write(template.render(path, template_val))
    def tables(self):
        template_val = {
        'static' : STATIC_FILES
        }
        path = os.path.join(TEMPLATE_PATH, 'tables.html')
        self.response.out.write(template.render(path, template_val))
    def typography(self):
        template_val = {
        'static' : STATIC_FILES
        }
        path = os.path.join(TEMPLATE_PATH, 'typography.html')
        self.response.out.write(template.render(path, template_val))