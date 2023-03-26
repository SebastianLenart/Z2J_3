from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = (
        Path.home() /
        "Z2J_3" /
        "knowledge" /
        "newsletter.pdf"
)

pdf_reader = PdfFileReader(str(pdf_path))

pdf_writer = PdfFileWriter()
pdf_writer.appendPagesFromReader(pdf_reader)
pdf_writer.encrypt(user_pwd="SuperSecret") # zeby usunac haslo trzeba zakomentowac

output_path = (
        Path.home() /
        "Z2J_3" /
        "knowledge" /
        "newsletter_protected.pdf"
)
with output_path.open(mode="wb") as output_file:
    pdf_writer.write(output_file)