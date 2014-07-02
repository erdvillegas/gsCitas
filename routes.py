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
	webapp2.Route(r'/blank', handler='handlers.sbHandler.SbAdmin', name='blank', handler_method='blank'),
	webapp2.Route(r'/buttons', handler='handlers.sbHandler.SbAdmin', name='buttons', handler_method='buttons'),
	webapp2.Route(r'/flot', handler='handlers.sbHandler.SbAdmin', name='flot', handler_method='flot'),
	webapp2.Route(r'/forms', handler='handlers.sbHandler.SbAdmin', name='forms', handler_method='forms'),
	webapp2.Route(r'/grid', handler='handlers.sbHandler.SbAdmin', name='grid', handler_method='grid'),
	webapp2.Route(r'/login', handler='handlers.sbHandler.SbAdmin', name='login', handler_method='login'),
	webapp2.Route(r'/morris', handler='handlers.sbHandler.SbAdmin', name='morris', handler_method='morris'),
	webapp2.Route(r'/notifications', handler='handlers.sbHandler.SbAdmin', name='notifications', handler_method='notifications'),
	webapp2.Route(r'/panels', handler='handlers.sbHandler.SbAdmin', name='panels', handler_method='panels'),
	webapp2.Route(r'/tables', handler='handlers.sbHandler.SbAdmin', name='tables', handler_method='tables'),
	webapp2.Route(r'/typography', handler='handlers.sbHandler.SbAdmin', name='typography', handler_method='typography'),
	webapp2.Route(r'/error', handler='handlers.sbHandler.SbAdmin', name='error', handler_method='error'),
	webapp2.Route(r'/exce', handler='handlers.sbHandler.SbAdmin', name='exce', handler_method='exce'),
]