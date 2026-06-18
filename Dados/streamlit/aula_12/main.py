import streamlit as st

pg = st.navigation(
    [st.Page('./pages/pdf_merger.py', title='PDF Merger'),
     st.Page('./pages/vizu_pdf.py', title='PDF Vizualizador')
    ],
    position='top'
)
pg.run()