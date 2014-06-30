import jinja2
import logging
import os, sys
import urllib
import webapp2


from handlers import BaseHandler
from lib.unipath import Path

PROYECTO = Path(__file__).ancestor(2)
RUTA = PROYECTO.child('templates')
logging.warning("RUTA - %s",RUTA )
TEMPLATE_ERROR = os.path.join(RUTA, 'error.html')
logging.warning("PATH - %s",TEMPLATE_ERROR )



def render_error(template_values):
    templateLoader = jinja2.FileSystemLoader(os.path.dirname(__file__))
    templateEnv = jinja2.Environment( loader=templateLoader )
    template = templateEnv.get_template(TEMPLATE_ERROR)
    outputText = template.render(templateVars)


def handle_404(request, response, exception):
    logging.exception(exception)
    response.set_status(404)
    template_values ={
    'tituloError' : 'Algo ha pasado ',
    'mensaje' : 'Oops! La pagina ya no esta por aqui'
    }
    render_error(template_values)

def handle_500(request, response, exception):
    logging.exception(exception)
    response.set_status(500)
    template_values ={
    'tituloError' : 'Algo ha pasado ',
    'mensaje' : ':( Algo paso con la pagina'
    }
    render_error(template_values)