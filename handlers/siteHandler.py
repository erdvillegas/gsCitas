#import lib.httpagentparser
import jinja2
import logging
import os
import logging
import urllib
import webapp2

from ConfigParser import ConfigParser
from google.appengine.api import users
from handlers.BaseHandler import *
from webapp2 import Router

 
class MainHandler(BaseHandler):
    def get(self):
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
        config = ConfigParser()
        config.read("config.ini")

        configuraciones = {
            #Dias disponibles
            'lunes' : config.get("configuraciones.Agenda","Lunes"),
            'martes' : config.get("configuraciones.Agenda","Martes"),
            'miercoles' : config.get("configuraciones.Agenda","Miercoles"),
            'jueves' : config.get("configuraciones.Agenda","Jueves"),
            'viernes' : config.get("configuraciones.Agenda","Viernes"),
            'sabado' : config.get("configuraciones.Agenda","Sabado"),
            'domingo' : config.get("configuraciones.Agenda","Domingo"),
            'desde' : config.get("configuraciones.Agenda","Desde"),
            'hasta' : config.get("configuraciones.Agenda","Hasta"),

            #Acciones del sitio
            'EnviarEmail' : config.get("configuraciones.Acciones","EnviarEmail"),
            'CualquieraAgenda' : config.get("configuraciones.Acciones","CualquieraAgenda"),
            'SitioActivado' : config.get("configuraciones.Acciones","SitioActivado"),
            'AgendaLlena' : config.get("configuraciones.Acciones","AgendaLlena")
        }
        logging.info("Configuraciones actuales: %s",configuraciones)
        self.render_template("config.html",**configuraciones)
    def citasMethod(self):
        self.render_template("citas.html")