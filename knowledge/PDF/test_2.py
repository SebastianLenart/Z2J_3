from pathlib import Path
from PyPDF2 import PdfFileReader

pdf_path = "C:\\Users\\Dell\\Z2J_3\\knowledge\\Pride_and_Prejudice.pdf"

# 1
pdf_reader = PdfFileReader(str(pdf_path))
output_file_path = "C:\\Users\\Dell\\Z2J_3\\knowledge\\output.txt"
# 2
with open(output_file_path, mode="w") as output_file:
# 3
    output_file.write(
    f"{pdf_reader.documentInfo.title}\n"
    f"Number of pages: {pdf_reader.getNumPages()}\n\n"
    )
# 4
    for page in pdf_reader.pages:
        text = page.extractText()
        output_file.write(text)

# 14.2