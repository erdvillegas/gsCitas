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
from webapp2 import Router
from unipath import path
import logging
from config import *


app = webapp2.WSGIApplication([
	webapp2.Route(r'/', handler='handlers.siteHandler.MainHandler', name='home'),
	webapp2.Route(r'/hola/<user>', handler='handlers.siteHandler.MainHandler', name='hola', handler_method='myMethod'),
	webapp2.Route(r'/ruta', handler='handlers.siteHandler.MainHandler', name='ruta', handler_method='ruta'),
	webapp2.Route(r'/agente', handler='handlers.siteHandler.MainHandler', name='ruta', handler_method='agente'),
	webapp2.Route(r'/device', handler='handlers.siteHandler.MainHandler', name='ruta', handler_method='device'),
], debug=DEBUG_SITE)