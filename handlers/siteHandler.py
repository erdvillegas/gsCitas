#import lib.httpagentparser
import jinja2
import os
import logging
import urllib
import webapp2

from config import *
from lib import httpagentparser
from webapp2_extras import jinja2
from webapp2_extras import json
from webapp2 import Router
from lib.ua_parser import *
from lib.user_agents import parse
from google.appengine.ext.webapp import template


class MainHandler(webapp2.RequestHandler):
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
    def jsonE(self):
        self.response.headers['Content-Type'] = 'application/json'
        obj = {
        'success': 'some var', 
        'payload': 'some var',
          } 
        self.response.write(json.encode(obj))
    def holaJS(self,user):
        self.response.headers['Content-Type'] = 'application/json'
        obj = {
        'Hola ': user,
          } 
        self.response.write(json.encode(obj))