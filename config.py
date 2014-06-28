import os,sys
import logging
import webapp2

from config import *
from lib.unipath import Path
from webapp2 import Router


BASE_DIR = os.path.realpath(os.path.dirname(__file__))
DEBUG_SITE = True

#Rutas Path
RUTA_PROYECTO = Path(__file__).ancestor(1)
TEMPLATE_PATH = RUTA_PROYECTO.child('templates')
STATIC_FILES = '/static/'

#Error Handler
def handle_404(request, response, exception):
    logging.exception(exception)
    template_args={
    'Errortitulo' : 'Algo a pasado',
    'mensaje' : 'Oops! I could swear this page was here!'
    }
    response.write(self.jinja2.render_template('error.html', **template_args))
    response.set_status(404)
def handle_500(request, response, exception):
    logging.exception(exception)
    template_args={
    'Errortitulo' : 'Algo a pasado',
    'mensaje' : 'A server error occurred!'
    }
    response.write(self.jinja2.render_template('error.html', **template_args))
    response.set_status(500)

#Templates Config

config = {}
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
