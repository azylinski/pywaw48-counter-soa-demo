from common.celery.factory import make_celery
from common.schedulers.back.back_tasks import BackTasks


class BackScheduler(object):
    def __init__(self, app_config):
        self._celery = make_celery(BackTasks.PREFIX, app_config)

    def business_logic(self):
        self._celery.send_task(BackTasks.BUSINESS_LOGIC, [])
