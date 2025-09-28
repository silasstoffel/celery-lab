import logging
import string
import time
from random import choices,randint
from .celery_client import celery_client

logging.basicConfig(level=logging.DEBUG)
TASK_NAME = 'payment_hub.create_payment'

@celery_client.task(name=TASK_NAME)
def create_payment(order: dict) -> None:
    characters = string.ascii_letters + string.digits
    random_string = ''.join(choices(characters, k=20))
    order_id = order.get('id', 'unknown')
    logging.info(f"Creating payment for order_id: {order_id}")
    time.sleep(4)  # Simulate some processing time
    payment_id = f"pay_{random_string}"
    logging.info(f"Payment created with payment_id: {payment_id} for order_id: {order_id}")

    statuses = ['authorized', 'error', 'timeout', 'pending', 'denied', 'refunded', 'canceled']
    index = randint(0, len(statuses) - 1)
    
    return {
        'id': payment_id,
        'status': statuses[index],
    }