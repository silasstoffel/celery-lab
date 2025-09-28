import random
from .tasks import process_payment, process_inventory

order_created = {
    'id': 1,
    'customer': 'Laptop',
    'quantity': 1,
    'total_price': 1200,
    'payments': [
        { 'method': 'credit_card', 'amount': 1200 }
    ]
}

if __name__ == '__main__':
    print('Order created, sending tasks to the queue...')
    
    event = order_created
    event['id'] = random.randint(100, 5000000)
    event['total_price'] = random.randint(10, 9000000)
    event['payments'][0]['amount'] = event['total_price']
    
    process_payment.delay(order_created)
    process_inventory.delay(order_created)
    print('Tasks sent!')

