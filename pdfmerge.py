# from py import PdfMerger
#  pip install PyPDF2
try:
    from PyPDF2 import PdfMerger
except ImportError:
    from pyPdf import PdfMerger

pdfs = ['pdf1.pdf', 'pdf2.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()
