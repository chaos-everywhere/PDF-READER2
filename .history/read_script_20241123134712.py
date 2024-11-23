import PyPDF2

reader = PyPDF2.PdfReader('chkoura_hamza_CV (2).pdf')

def toto():

    print(len(reader.pages))

    print(reader.pages[0].extract_text())




if __name__ == "__main__":
    toto()

