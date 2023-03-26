from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = (
        Path.home() /
        "Z2J_3" /
        "knowledge" /
        "newsletter_protected.pdf"
)

pdf_reader = PdfFileReader(str(pdf_path))
pdf_reader.decrypt(password="SuperSecret")
""" return:
0 indicates the password is incorrect
1 indicates the user password was matched
2 indicated the owner password was matched
"""
print(pdf_reader.getPage(0))









