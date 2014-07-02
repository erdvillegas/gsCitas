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
import logging
import webapp2

from config import *
from ErrorHandler import *
from lib.unipath import path
from routes import _routes
from webapp2 import Router
from webapp2_extras import jinja2

 
app = webapp2.WSGIApplication(_routes, debug=DEBUG_SITE,config=config)

app.error_handlers[404] = handle_404
app.error_handlers[500] = handle_500