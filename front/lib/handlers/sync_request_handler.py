# 
# FRONT
#

from tornado.web import RequestHandler


class SyncReqestHandler(RequestHandler):
    def initialize(self, back_client, *args, **kwargs):
        super(SyncReqestHandler, self).initialize(*args, **kwargs)
        self._back_client = back_client

    def get(self):
        self._back_client.business_logic()
        html = "<h2>GET /sync :</h2>"\
        	"<h1>HTTP Request to BACK APP</h1>"
        self.finish(html)
