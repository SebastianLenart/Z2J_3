from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = (
        Path.home() /
        "Z2J_3" /
        "knowledge" /
        "expense_reports" /
        "chapter1.pdf"
)

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

for n in range(pdf_reader.getNumPages()):
    page = pdf_reader.getPage(n)
    if n % 2 == 0:
        page.rotateClockwise(90)
    pdf_writer.addPage(page)

with Path("ugly_rotated.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

#     zmiana zapisuje sie w informacji o stronie!!! pdf_reader.getPage(0)
page = pdf_reader.getPage(0)
print(page["/Rotate"])  # 90
print(page)  # 90
print("*"*10)
page = pdf_reader.getPage(1) # brak rotatcji to brak klucza!!!!!!
print(page)
print("*"*10)
page = pdf_reader.getPage(2)
print(page)  # 0
