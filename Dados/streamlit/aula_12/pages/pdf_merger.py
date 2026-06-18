import streamlit as st
from utils.obter_pdfs import obter_pdf
from utils.juntar_pdfs import juntar_pdfs

st.set_page_config(page_title='PDF Merger', layout='centered')

st.title('PDF Merger')

final_file = st.text_input(
    label = 'Nome do arquivo',
    placeholder = 'Digite o nome do arquivo final'
)

files = st.file_uploader(
    label = 'Arquivos',
    type = 'pdf',
    accept_multiple_files = True
)

colums = st.columns(5)

with colums[2]:
    botao = st.button('Juntar PDFs')

if botao:
    pdfs = obter_pdf(files)
    pdf_certo = juntar_pdfs(pdfs)
    st.download_button(
        label = 'Download',
        data = pdf_certo,
        file_name = f'{final_file}.pdf',
        mime='application/octet-stream'
    )