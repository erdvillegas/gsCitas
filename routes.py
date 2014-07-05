import logging
import webapp2

from webapp2 import Router

_routes = [
	webapp2.Route(r'/hola/<user>', handler='handlers.siteHandler.MainHandler', name='hola', handler_method='myMethod'),
	webapp2.Route(r'/ruta', handler='handlers.siteHandler.MainHandler', name='ruta', handler_method='ruta'),
	webapp2.Route(r'/agente', handler='handlers.siteHandler.MainHandler', name='ruta', handler_method='agente'),
	webapp2.Route(r'/device', handler='handlers.siteHandler.MainHandler', name='ruta', handler_method='device'),
	webapp2.Route(r'/os', handler='handlers.siteHandler.MainHandler', name='ruta', handler_method='opsi'),
    
    #SB-ADMIN-V2
	webapp2.Route(r'/', handler='handlers.sbHandler.SbAdmin', name='home'),
	webapp2.Route(r'/login', handler='handlers.sbHandler.SbAdmin', name='login', handler_method='login'),
	webapp2.Route(r'/error', handler='handlers.sbHandler.SbAdmin', name='error', handler_method='error'),
	webapp2.Route(r'/exce', handler='handlers.sbHandler.SbAdmin', name='exce', handler_method='exce'),
]