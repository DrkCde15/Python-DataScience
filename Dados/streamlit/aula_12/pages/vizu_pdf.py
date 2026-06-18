import streamlit as st

st.set_page_config(page_title='PDF Vizualizador', layout='centered')

st.title('PDF Vizualizador')

upload = st.file_uploader(
    label = 'Arquivos',
    type = ['pdf']
    )

if upload:
    st.pdf(upload, height=850)