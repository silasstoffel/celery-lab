import logging
import random
from .celery_client import celery_client

logging.basicConfig(level=logging.DEBUG)

TASK_NAME = 'payment_hub.create_payment'

def send_order_to_create_payment():
    id = random.randint(100, 5000000)
    price = random.randint(10, 9000000)

    order_created = {
        'id': id,
        'customer': 'Laptop',
        'quantity': 1,
        'total_price': price,
        'payments': [
            { 'method': 'credit_card', 'amount': price }
        ]
    }
    task_id = f"task_{id}" 
    
    celery_client.send_task(
        TASK_NAME, 
        args=[order_created],
        task_id=task_id
    )
    logging.info(f'Order created. [order_id={id}, task_id={task_id}]')

if __name__ == '__main__':
    send_order_to_create_payment()