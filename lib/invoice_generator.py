from pathlib import Path
from typing import BinaryIO

import borb.pdf
from borb.pdf import Document, Page, SingleColumnLayout, Paragraph, PDF


class InvoiceGenerator:
    @staticmethod
    def generate():
        # empty document
        pdf = Document()
        
        # add page
        page = Page()
        pdf.add_page(page)
        
        # use layout
        layout = SingleColumnLayout(page)
        
        # add paragraph
        layout.add(Paragraph("Hello Hallo"))
        
        # store
        with open(Path("output.pdf"), "wb") as pdf_file_handle:
            PDF.dumps(pdf_file_handle, pdf)
        
        