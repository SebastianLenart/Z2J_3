from pathlib import Path
from PyPDF2 import PdfFileMerger

report_dir = (
        Path.home() /
        "Z2J_3" /
        "knowledge" /
        "expense_reports"
)
report_path = report_dir / "chapter1.pdf"
toc_path = report_dir / "first_page.pdf"

pdf_merger = PdfFileMerger()
pdf_merger.append(str(report_path))
pdf_merger.merge(1, str(toc_path)) # w dowolne miejsce mozna wstawic plik pdf, append tylko na koncu

with Path("full_report.pdf").open(mode="wb") as output_file:
    pdf_merger.write(output_file)
