from PyPDF2 import PdfFileReader
from pathlib import Path

file_path = "C:\\Users\\Dell\\Z2J_3\\knowledge\\Pride_and_Prejudice.pdf"
input_pdf = PdfFileReader(file_path)
print(input_pdf.getNumPages())
print(input_pdf.getDocumentInfo())
print(input_pdf.getDocumentInfo().title)
print(input_pdf.getDocumentInfo().author)
print(type(input_pdf.getDocumentInfo()))
##########
first_page = input_pdf.getPage(0)
# print(first_page.extractText())
# wszystkie strony:
# for page in input_pdf.pages:
#     print(page.extractText())
print(type(first_page))
print(Path.home())
