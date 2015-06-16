# 
# FRONT
#

from tornado.web import RequestHandler


class CounterReqestHandler(RequestHandler):
    def initialize(self, back_client, *args, **kwargs):
        super(CounterReqestHandler, self).initialize(*args, **kwargs)
        self._back_client = back_client

    def get(self):
        response = self._back_client.get_count()
        data = response.json()
        count = data['result'] if data['result'] else 0
        html = "<h2>GET /:</h2>"\
    		"<h1>PyWaw #{} and counting</h1>".format(count)
        self.finish(html)
