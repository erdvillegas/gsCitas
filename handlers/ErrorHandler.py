import logging
import webapp2
from handlers import BaseHandler

class ErrorHandler(webapp2.BaseHandlerAdapter):
    def __call__(self, request, response, exception):
        request.route_args = {}
        request.route_args['exception'] = exception
        handler = self.handler(request, response)
        return handler.get()

class Handle404(BaseHandler):
    def get(self):
        self.render(filename="404.html",
            page_title="404",
            exception=self.request.route_args['exception']
        )