from pypdf import PdfWriter

def juntar_pdfs(pdfs):
    writer = PdfWriter()
    for pdf in pdfs:
        writer.append(pdf)
    writer.write('file_temp.pdf')
    writer.close()
    
    with open('file_temp.pdf', 'rb') as f:
        pdf_certo = f.read()
    return pdf_certo