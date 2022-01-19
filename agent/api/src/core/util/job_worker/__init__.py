from celery import Celery, chain
import os

# TODO: Raise an error when celery app couldn't start up
job_queue_app = Celery(
    'tasks', broker=f'redis://{os.getenv("REDIS_USER")}:{os.getenv("REDIS_PASSWORD")}@{os.getenv("BROKER_HOST")}:6379/0')
job_chain = chain
