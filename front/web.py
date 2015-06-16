# 
# FRONT
#

import tornado.ioloop
from tornado.web import Application
from tornado.options import options
from common.clients.back.back_client import BackClient
from common.schedulers.back.back_scheduler import BackScheduler
from lib import handlers
from config.config_base import ConfigBase


ConfigBase.setup()

# Load clients
back_client = BackClient(options.back_client_api_url)
back_scheduler = BackScheduler(options.back_celery_config)

# Routing
application = Application([
	# Sync
    (r"/", handlers.CounterReqestHandler, dict(back_client=back_client)),
    (r"/sync", handlers.SyncReqestHandler, dict(back_client=back_client)),
	# Async
    (r"/async", handlers.AsyncReqestHandler, dict(back_scheduler=back_scheduler))
], debug=True)


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()