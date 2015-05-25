import logging
import webapp2

from webapp2 import Router

_routes = [
    #SB-ADMIN-V2
	webapp2.Route(r'/', handler='handlers.siteHandler.MainHandler', name='home'),
	webapp2.Route(r'/login', handler='handlers.siteHandler.MainHandler', name='login', handler_method='login'),

	#SideBar Menu
	webapp2.Route(r'/perfil', handler='handlers.siteHandler.ServiciosHandler', name='perfil', handler_method='perfilMethod'),
	webapp2.Route(r'/pacientes', handler='handlers.siteHandler.ServiciosHandler', name='pacientes', handler_method='pacientesMethod'),
	webapp2.Route(r'/citas', handler='handlers.siteHandler.ServiciosHandler', name='citas', handler_method='citasMethod'),
	webapp2.Route(r'/config', handler='handlers.siteHandler.ServiciosHandler', name='config', handler_method='configMethod'),

	#Logica de aplicacion
	webapp2.Route(r'/detallePaciente/<pacienteID>', handler='handlers.siteHandler.SchedulerHandler', name='detalles_paciente', handler_method='detallePacienteMethod'),
]