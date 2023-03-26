from PyPDF2 import PdfFileMerger
from pathlib import Path

reports_dir = (
        Path.home() /
        "Z2J_3" /
        "knowledge" /
        "expense_reports"
)

pdf_merger = PdfFileMerger()

expense_reports = list(reports_dir.glob("*.pdf"))
expense_reports.sort()
for path in expense_reports:
    pdf_merger.append(str(path))

with Path("expense_reports.pdf").open(mode="wb") as output_file:
    pdf_merger.write(output_file)












