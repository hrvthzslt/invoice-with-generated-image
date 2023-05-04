from decouple import config
from lib.image_generator import ImageGenrator
from lib.invoice_generator import InvoiceGenerator

#image_url = ImageGenrator(key=config('OPENAI_API_KEY')).generate("cool coding people with computers")
# print(image_url)
InvoiceGenerator.generate()
