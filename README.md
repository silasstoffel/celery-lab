# Commands

## Setup

```sh
#install pyenv
curl https://pyenv.run | bash

pyenv local 3.12.11

python -m venv .venv

source .venv/bin/activate

#deactivate

#poetry
curl -sSL https://install.python-poetry.org | python3 -

poetry install
```

## Shared source code

```sh

# Run producer
python3 -m src.producer

# Run Producer for each 1 second
watch -n 1  python3 -m src.producer

# Run consumers
celery -A src.celery_app worker --loglevel=INFO
```

## Micro service simulations

```sh
# Order service produce message
python3 -m src.order_service.create_order

# Payment hub consumes the message and creates a payment
celery -A src.payment_hub.celery_client worker --loglevel=INFO
```