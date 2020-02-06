import argparse
import os
import sys
from PyPDF2 import PdfFileMerger, PdfFileWriter, PdfFileReader

# Parse arguments of -o: Use m for merge, s for slice
parser = argparse.ArgumentParser()
parser.add_argument("-o","--option", choices=['m', 's', 'M', 'S'],
                    help="Choose what you would like to do. m [merge], s [slice]")
args = parser.parse_args()

# PDF merge function.
# Asks how many PDF's to merge and asks for file names.
def mergepdf():
	merger = PdfFileWriter()
	num = int(input("How many PDF's do you want to merge together: "))
	pdflist = []
	for x in range(num):
		pdflist.append(input("Enter PDF name: "))
	for path in pdflist:
		pdf_reader = PdfFileReader(path)
		print(path)
		if pdf_reader.isEncrypted:
			pdf_reader.decrypt('')
		for page in range(pdf_reader.getNumPages()):
			# Add each page to the writer object
			merger.addPage(pdf_reader.getPage(page))
#    for filen in pdflist:
#       merger.append(PdfFileReader(filen))
	with open('merged-docs.pdf', 'wb') as out:
		merger.write(out)
	print("Done.")

# PDF slice function
# Asks filename of PDF and slices depending on page numbers.
def slicepdf():
    pdfname = input("Which PDF do you want to slice: ")
    pgnums = input("Choose pages separated by a comma (,): ")
    x = pgnums.split(',')
    reader = PdfFileReader(pdfname)
    slicer = PdfFileWriter()
    for pg in x:
        slicer.addPage(reader.getPage(int(pg)-1))
    output_file = "sliced-doc.pdf"
    with open(output_file, 'wb') as out:
        slicer.write(out)

if __name__ == "__main__":
    if args.option == 'm' or args.option == 'M':
        mergepdf()
    elif args.option == 's' or args.option == 'S':
        slicepdf()
    else:
        print("Not a valid input, goodbye")
