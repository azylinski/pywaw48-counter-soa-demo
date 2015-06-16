# 
# FRONT
#

from tornado.web import RequestHandler


class AsyncReqestHandler(RequestHandler):
    def initialize(self, back_scheduler, *args, **kwargs):
        super(AsyncReqestHandler, self).initialize(*args, **kwargs)
        self._back_scheduler = back_scheduler

    def get(self):
        self._back_scheduler.business_logic()
        html = "<h2>GET /async :</h2><h1>Send Celery Task to BACK APP</h1>"
        self.finish(html)
