from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter
import copy


pdf_path = (
        Path.home() /
        "Z2J_3" /
        "knowledge" /
        "split_and_rotate.pdf"
)

pdf_reader = PdfFileReader(str(pdf_path))
first_page = pdf_reader.getPage(0)
print(first_page.mediaBox) # RectangleObject([0, 0, 792, 612])
print(first_page.mediaBox.lowerLeft)
print(first_page.mediaBox.upperRight)
print(first_page.mediaBox.upperRight[1])
first_page.mediaBox.upperRight = (0, 480)

pdf_writer = PdfFileWriter()
# pdf_writer.addPage(first_page)
# with Path("cropped_page.pdf").open(mode="wb") as output_file:
#     pdf_writer.write(output_file)

left_side = copy.deepcopy(first_page)
current_coords = left_side.mediaBox.upperRight
new_coords = (current_coords[0] / 2, current_coords[1])
left_side.mediaBox.upperRight = new_coords

right_side = copy.deepcopy(first_page)
right_side.mediaBox.upperLeft = new_coords

pdf_writer.addPage(left_side)
pdf_writer.addPage(right_side)
with Path("cropped_pages.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)