import PyPDF2

reader = PyPDF2.PdfReader('example.pdf')

print(len(reader.pages))
