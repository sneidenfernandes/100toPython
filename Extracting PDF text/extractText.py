from PyPDF2 import PdfReader

reader = PdfReader("sample.pdf")


for i in range(len(reader.pages)):
    page = reader.pages[i]
    print(page.extract_text())


