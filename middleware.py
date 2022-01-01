import os
from werkzeug.wrappers import Request, Response, ResponseStream


class middleware():

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)

        if request.headers.get("auth") and request.headers.get("auth") == os.environ.get("HEADER_KEY"):
            environ['auth'] = {'message': 'Auth Success'}
            return self.app(environ, start_response)

        res = Response(u'Authorization failed',
                       mimetype='text/plain', status=401)
        return res(environ, start_response)
