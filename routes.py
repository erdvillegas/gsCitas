import logging
import webapp2

from webapp2 import Router

_routes = [
    #SB-ADMIN-V2
	webapp2.Route(r'/', handler='handlers.siteHandler.MainHandler', name='home'),
	webapp2.Route(r'/login', handler='handlers.siteHandler.MainHandler', name='login', handler_method='login'),

	#Rutas de servicio
	webapp2.Route(r'/config', handler='handlers.siteHandler.ServiciosHandler', name='config', handler_method='configMethod'),
	webapp2.Route(r'/citas', handler='handlers.siteHandler.ServiciosHandler', name='citas', handler_method='citasMethod'),
]