# Commands

## Setup

```sh
#install pyenv
curl https://pyenv.run | bash

# setting python version
pyenv local 3.12.11

# enabling venv 
python -m venv .venv

# Activating specific python version
source .venv/bin/activate

# Deactivating local version
#deactivate

# Install poetry
curl -sSL https://install.python-poetry.org | python3 -

#install version
poetry install
```

## Shared source code (Monolith Arch)

```sh

# Run producer
python3 -m src.producer

# Run Producer for each 1 second
watch -n 1  python3 -m src.producer

# Run consumers
celery -A src.celery_app worker --loglevel=INFO
```

## Micro Service simulations

```sh
# Order service produce message
python3 -m src.order_service.create_order

# Payment hub consumes the message and creates a payment
celery -A src.payment_hub.celery_client worker --loglevel=INFO
```