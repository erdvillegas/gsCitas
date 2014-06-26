import webapp2
from webapp2 import Router
import os,sys
from unipath import Path
import logging

BASE_DIR = os.path.realpath(os.path.dirname(__file__))
DEBUG_SITE = True

#Rutas Path
RUTA_PROYECTO = Path(__file__).ancestor(1)
TEMPLATE_PATH = RUTA_PROYECTO.child('templates')
STATIC_FILES = RUTA_PROYECTO.child('static')

#Error Handler

vat = {
	'BASE_DIR' : BASE_DIR,
	'DEBUG_SITE' : DEBUG_SITE,
	'RUTA_PROYECTO' : RUTA_PROYECTO,
	'TEMPLATE_PATH' : TEMPLATE_PATH,
	'STATIC_FILES' : STATIC_FILES,
	'TEST' : os.getcwd(),
}