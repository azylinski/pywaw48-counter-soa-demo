# General
DEBUG = True

# Celery
CELERY_BROKER_URL = 'amqp://rabbit'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# Redis
REDIS_HOST = 'redis'
REDIS_PORT = 6379
