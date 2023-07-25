# from py import PdfMerger
#  pip install PyPDF2
import argparse

arg_parser = argparse.ArgumentParser( description = "Copy source_file as target_file." )
arg_parser.add_argument( "name_merged_file" )
arg_parser.add_argument( "first_file" )
arg_parser.add_argument( "second_file" )
arguments = arg_parser.parse_args()

first_file = arguments.first_file
second_file = arguments.second_file
name_merged_file = arguments.name_merged_file
print( "Copying [{}] to [{}]".format(source, target) )
try:
    from PyPDF2 import PdfMerger
except ImportError:
    from pyPdf import PdfMerger

pdfs = [first_file, second_file]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

if '.pdf' not in name_merged_file:
    name_merged_file = name_merged_file + '.pdf'
merger.write(name_merged_file)
merger.close()
