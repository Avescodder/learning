from PyPDF2 import PdfReader, PdfWriter
from pages import chapters

file_name = r'textbook.pdf'

for i in range(len(chapters)):
    pages = chapters[i]
    reader = PdfReader(file_name)
    writer = PdfWriter()
    page_range = range(pages[0], pages[1] + 1)

    for page_num, page in enumerate(reader.pages, 1):
        if page_num in page_range:
            writer.add_page(page)

    with open(f'{file_name}_page_{pages[0]}-{pages[1]}.pdf', 'wb') as out:
        writer.write(out)