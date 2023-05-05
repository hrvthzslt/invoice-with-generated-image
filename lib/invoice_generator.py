from pathlib import Path

from borb.io.read.types import Decimal
from borb.pdf import Document, Page, SingleColumnLayout, Paragraph, PDF, Image


class InvoiceGenerator:
    @staticmethod
    def generate(products: list, image_url: str):
        # empty document
        pdf = Document()

        # add page
        page = Page()
        pdf.add_page(page)

        # use layout
        layout = SingleColumnLayout(page)

        layout.add(Paragraph("Invoice:", font_size=Decimal(24), font="Helvetica"))

        # add image
        layout.add(
            Image(
                image_url,
                width=Decimal(256),
                height=Decimal(256),
            ))

        # add paragraphs
        layout.add(Paragraph("Purchased produts:", font_size=Decimal(24), font="Helvetica"))
        for product in products:
            layout.add(Paragraph(product, font_size=Decimal(14), font="Helvetica"))

        # store
        with open(Path("output.pdf"), "wb") as pdf_file_handle:
            PDF.dumps(pdf_file_handle, pdf)
