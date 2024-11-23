import PyPDF2

reader = PyPDF2.PdfReader('chkoura_hamza_CV (2).pdf')

print(len(reader.pages))

print(reader.pages[0].extract_text())
