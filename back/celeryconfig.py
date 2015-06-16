from datetime import timedelta

def to_seconds(*args, **kwargs):
    return timedelta(*args, **kwargs).total_seconds()


CELERY_BROKER_URL = 'amqp://rabbit'
# CELERY_RESULT_BACKEND = 'redis://redis'


# When a task has been executed, the data returned by the function is stored
# in a database. To save space we limit the time that the results are stored.
# By default, this is 7 days, but it can be changed with this setting.
CELERY_TASK_RESULT_EXPIRES = to_seconds(days=7)
# By default it is assumed that your task does not write any result files, but
# returns the results. If your task stores the results in files instead, you
# should set this to True and modify the `delete_old_files` task in `app.py`
# to delete the result files, wherever you choose to store them.
CELERY_IGNORE_RESULT = False


# Warn about shutdown after 10 min.
CELERYD_TASK_SOFT_TIME_LIMIT = to_seconds(minutes=10)
# Force shutdown after 11 min.
CELERYD_TASK_TIME_LIMIT = to_seconds(minutes=11)


CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'


# CELERYBEAT_SCHEDULE = {
#     'delete_old_files': {
#         'task': 'app.delete_old_files',
#         'schedule': timedelta(hours=1),
#         'args': (CELERY_TASK_RESULT_EXPIRES,)
#     },
# }
