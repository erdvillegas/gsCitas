import webapp2
from webapp2 import Router
import os,sys
from unipath import Path
import logging

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DEBUG_SITE = True

#Rutas Path
RUTA_PROYECTO = Path(__file__).ancestor(1)
TEMPLATE_PATH = RUTA_PROYECTO.child('templates')
STATIC_FILES = RUTA_PROYECTO.child('static')

#Error Handler
