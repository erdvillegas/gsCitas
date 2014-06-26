import os
import jinja2
import webapp2
import logging
from webapp2 import Router
from config import *
import httpagentparser
from ua_parser import *
from user_agents import parse

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Hello World")
    def myMethod(self,user):
        self.response.write("Hola " + user)
    def ruta(self):
    	self.response.write(self.request.application_url)
    def agente(self):
    	agente = self.request.headers.get('User-Agent')
    	device = httpagentparser.simple_detect(agente)
    	self.response.write(device)
    def device(self):
    	agente = self.request.headers.get('User-Agent')
    	device = httpagentparser.detect(agente)
    	ua_string = agente
    	user_agent = parse(ua_string)
    	self.response.write(user_agent.is_touch_capable)