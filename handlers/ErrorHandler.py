import jinja2
import logging
import os
import urllib
import webapp2


from handlers import BaseHandler


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def render_error(template_values):
	 template = JINJA_ENVIRONMENT.get_template('error.html')
	 response.write(template.render(template_values))


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