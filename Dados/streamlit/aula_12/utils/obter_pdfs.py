from pypdf import PdfReader

def obter_pdf(arquivos):
    pdfs = []
    for a in arquivos:
        reader = PdfReader(a)
        pdfs.append(reader)
    return pdfs