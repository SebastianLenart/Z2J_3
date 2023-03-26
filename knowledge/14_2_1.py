from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path2 = "C:\\Users\\Dell\\Z2J_3\\knowledge\\Pride_and_Prejudice.pdf"
pdf_path = "C:\\Users\\Sebastian\\Z2J_3\\knowledge\\Pride_and_Prejudice.pdf"
input_pdf = PdfFileReader(pdf_path)
first_page = input_pdf.getPage(0)
pdf_writer = PdfFileWriter()

# for n in range(1, 4):
#     page = input_pdf.getPage(n)
#     pdf_writer.addPage(page)

# or shorter

for page in input_pdf.pages[1:4]:
    pdf_writer.addPage(page)

with Path("chapter1.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

"""
pdf_writer = PdfFileWriter()
pdf_writer.appendPagesFromReader(pdf_reader)

"""
