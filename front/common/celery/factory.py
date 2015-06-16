from celery import Celery


def make_celery(main_name, app_config):
    celery = Celery(main_name, broker=app_config['CELERY_BROKER_URL'])
    celery.conf.update(app_config)
    return celery
