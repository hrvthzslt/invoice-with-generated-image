# Invoice with generated image

## Setup

Create `.env` using `.env.example`. You will need an OpenAI Api key.

## Run

### Start venv

```shell
python -m venv venv
source venv/bin/activate
```

### Run invoice generation

Run invoice-pictures with the list of products which you want to be included in the invoice.

```shell
python invoice-picture.py 'keyboard' 'mouse'
```

### Exit venv

```shell
deactivate
```