import os
import webapp2
import logging
from webapp2 import Router
import httpagentparser
from ua_parser import *
from user_agents import parse
from config import *
from google.appengine.ext.webapp import template


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