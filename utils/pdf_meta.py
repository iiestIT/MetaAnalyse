from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

def pdf_meta(pdf, pwd=None):
    with open(pdf, "rb") as f:
        parser = PDFParser(f)
        doc = PDFDocument(parser, password=pwd)

    return doc