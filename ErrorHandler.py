import logging
import main
import os, sys
import urllib
import webapp2

from handlers import BaseHandler
from lib.unipath import Path
from webapp2_extras import jinja2


def render_error(response,template_values):
    jinja=jinja2.get_jinja2(app=main.app)
    response.write(jinja.render_template('error.html', **template_values))

def handle_404(request, response, exception):
    logging.exception(exception)
    response.set_status(404)
    template_values ={
    'ErrorTitulo' : 'Algo ha pasado ',
    'mensaje' : 'Oops! La pagina ya no esta por aqui'
    }
    render_error(response,template_values)

def handle_500(request, response, exception):
    logging.exception(exception)
    response.set_status(500)
    template_values ={
    'ErrorTitulo' : 'Algo ha pasado ',
    'mensaje' : ':( Algo paso con la pagina'
    }
    render_error(response,template_values)