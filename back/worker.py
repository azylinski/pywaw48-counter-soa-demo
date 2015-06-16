# 
# BACK
#

from flask import Flask
from redis import Redis
from common.celery.factory import make_celery
from common.schedulers.back.back_tasks import BackTasks
from lib.managers.core_manager import CoreManager


app = Flask(__name__)
app.config.from_envvar('APP_CONFIG')
celery = make_celery(BackTasks.PREFIX, app.config)

# Register managers
redis = Redis(host=app.config['REDIS_HOST'],
	          port=app.config['REDIS_PORT'])
core_manager = CoreManager(redis)


@celery.task(name=BackTasks.BUSINESS_LOGIC, bind=True)
def business_logic(self):
    # print 'Celery task: business_logic'
    core_manager.business_logic()
    return "OK!"
