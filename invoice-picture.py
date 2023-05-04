from decouple import config
from lib.image_generator import ImageGenrator
from lib.invoice_generator import InvoiceGenerator

products = ['2 pizza', '1 amiga 500']
print(' '.join(products))
InvoiceGenerator.generate(
    products,
    ImageGenrator(key=config('OPENAI_API_KEY')).generate(' '.join(products))
)

print('Invoice created')
