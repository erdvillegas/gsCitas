import os,sys
import logging
import main
import webapp2

from config import *
import ErrorHandler
from lib.unipath import Path
from webapp2 import Router
from webapp2_extras import jinja2

BASE_DIR = os.path.realpath(os.path.dirname(__file__))
DEBUG_SITE = True

#Rutas Path
RUTA_PROYECTO = Path(__file__).ancestor(1)
TEMPLATE_PATH = RUTA_PROYECTO.child('templates')
STATIC_FILES = '/static/'
ERROR_TEMPLATE_FILE = 'error.html'

#Templates Config

config = {
  'webapp2_extras.auth': {
    'user_model': 'models.User',
    'user_attributes': ['name']
  },
  'webapp2_extras.sessions': {
    'secret_key': 'YOUR_SECRET_KEY'
  }
}

config['webapp2_extras.jinja2'] = {
    'template_path': 'templates',
    'compiled_path': None,
    'force_compiled': False,
    'environment_args': {
        'autoescape': True,
        'extensions': [
            'jinja2.ext.autoescape',
            'jinja2.ext.with_'
            ]
        },
    'globals': {
        'url_for' : webapp2.uri_for,
        'static' : STATIC_FILES,
        },
    'filters': None,
    }