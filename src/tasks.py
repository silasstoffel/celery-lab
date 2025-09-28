import time
from src.celery_app import celery_app


@celery_app.task
def process_payment(order):
    order_id = order.get('id', 'unknown')
    print(f'Processing payment for order {order_id}')
    time.sleep(3)
    print(f'Payment created successfully Order {order_id}')


@celery_app.task
def process_inventory(order):
    order_id = order.get('id', 'unknown')
    print(f'Processing inventory for order {order_id}')
    time.sleep(2)
    print(f'Inventory processed successfully. Order {order_id}')
