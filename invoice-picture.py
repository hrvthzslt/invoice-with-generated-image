from sys import argv
from decouple import config
from lib.image_generator import ImageGenrator
from lib.invoice_generator import InvoiceGenerator


def main():
    argv.pop(0)

    InvoiceGenerator.generate(
        argv,
        ImageGenrator(key=config('OPENAI_API_KEY')).generate(' '.join(argv))
    )

    print('Invoice created')


if __name__ == "__main__":
    main()
