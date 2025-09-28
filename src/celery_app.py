from celery import Celery

celery_app = Celery(
    'celery_lab', 
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/1',
    include=['src.tasks']
)

celery_app.conf.update(
    task_serializer='json',
    result_serializer='json',
    accept_content=['json'],
    timezone='UTC',
    enable_utc=True,
)
