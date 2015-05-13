import logging
import webapp2

from webapp2 import Router

_routes = [
    #SB-ADMIN-V2
	webapp2.Route(r'/', handler='handlers.siteHandler.MainHandler', name='home'),
	webapp2.Route(r'/login', handler='handlers.siteHandler.MainHandler', name='login', handler_method='login'),
	webapp2.Route(r'/error', handler='handlers.siteHandler.MainHandler', name='error', handler_method='error'),
	webapp2.Route(r'/exce', handler='handlers.siteHandler.MainHandler', name='exce', handler_method='exce'),

]