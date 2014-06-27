#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os, sys
import webapp2
import logging
from webapp2 import Router
from unipath import path
from config import *

 
app = webapp2.WSGIApplication([
	webapp2.Route(r'/', handler='handlers.siteHandler.MainHandler', name='home'),
	webapp2.Route(r'/hola/<user>', handler='handlers.siteHandler.MainHandler', name='hola', handler_method='myMethod'),
	webapp2.Route(r'/ruta', handler='handlers.siteHandler.MainHandler', name='ruta', handler_method='ruta'),
	webapp2.Route(r'/agente', handler='handlers.siteHandler.MainHandler', name='ruta', handler_method='agente'),
	webapp2.Route(r'/device', handler='handlers.siteHandler.MainHandler', name='ruta', handler_method='device'),
	webapp2.Route(r'/os', handler='handlers.siteHandler.MainHandler', name='ruta', handler_method='opsi'),
    #SB-ADMIN-V2
	webapp2.Route(r'/sb', handler='handlers.siteHandler.SbAdmin', name='sb'),
	webapp2.Route(r'/blank', handler='handlers.siteHandler.SbAdmin', name='blank', handler_method='blank'),
	webapp2.Route(r'/buttons', handler='handlers.siteHandler.SbAdmin', name='buttons', handler_method='buttons'),
	webapp2.Route(r'/flot', handler='handlers.siteHandler.SbAdmin', name='flot', handler_method='flot'),
	webapp2.Route(r'/forms', handler='handlers.siteHandler.SbAdmin', name='forms', handler_method='forms'),
	webapp2.Route(r'/grid', handler='handlers.siteHandler.SbAdmin', name='grid', handler_method='grid'),
	webapp2.Route(r'/login', handler='handlers.siteHandler.SbAdmin', name='login', handler_method='login'),
	webapp2.Route(r'/morris', handler='handlers.siteHandler.SbAdmin', name='morris', handler_method='morris'),
	webapp2.Route(r'/notifications', handler='handlers.siteHandler.SbAdmin', name='notifications', handler_method='notifications'),
	webapp2.Route(r'/panels', handler='handlers.siteHandler.SbAdmin', name='panels', handler_method='panels-wells'),
	webapp2.Route(r'/tables', handler='handlers.siteHandler.SbAdmin', name='tables', handler_method='tables'),
	webapp2.Route(r'/typography', handler='handlers.siteHandler.SbAdmin', name='typography', handler_method='typography'),
], debug=DEBUG_SITE)