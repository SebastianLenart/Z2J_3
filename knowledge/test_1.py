from PyPDF2 import PdfFileReader

file_path = "C:\\Users\\Sebastian\\Z2J_3\\knowledge\\Pride_and_Prejudice.pdf"
input_pdf = PdfFileReader(file_path)
print(input_pdf.getNumPages())
print(input_pdf.getDocumentInfo())
print(input_pdf.getDocumentInfo().title)
print(input_pdf.getDocumentInfo().author)
print(type(input_pdf.getDocumentInfo()))

# 348