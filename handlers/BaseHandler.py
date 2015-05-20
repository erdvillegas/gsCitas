import logging
import webapp2
from webapp2_extras import jinja2
from webapp2_extras import json

class BaseHandler(webapp2.RequestHandler): 
    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)
    def render_template(self, filename, **template_args):
        self.response.write(self.jinja2.render_template(filename, **template_args))
    def renderJson(self, obj):
		self.response.headers['Content-Type'] = 'application/json'
		self.response.write(json.encode(obj))
    def mi_error(self,mensaje):
	    logging.error(mensaje)
	    template_args={
	    'Errortitulo' : 'Algo a pasado',
	    'mensaje' : mensaje
	    }
	    self.response.write(self.jinja2.render_template('error.html', **template_args))