import logging
import webapp2

from webapp2 import Router

_routes = [
    #SB-ADMIN-V2
	webapp2.Route(r'/', handler='handlers.siteHandler.MainHandler', name='home'),
	webapp2.Route(r'/login', handler='handlers.siteHandler.MainHandler', name='login', handler_method='login'),

	#Rutas de servicio
	webapp2.Route(r'/config', handler='handlers.siteHandler.ServiciosHandler', name='configuracion', handler_method='configMethod'),
]