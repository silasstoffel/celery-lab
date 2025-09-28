from celery import Celery

celery_client = Celery(
    'order_service', 
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/1',
    include=[]
)

celery_client.conf.update(
    task_serializer='json',
    result_serializer='json',
    accept_content=['json'],
    timezone='UTC',
    enable_utc=True,
)
