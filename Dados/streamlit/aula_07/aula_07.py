import streamlit as st
import time

st.set_page_config(
    page_title="Customization Webpage",
    page_icon="👋",
    layout="wide"
)

st.title('Customization and Components')

st.header('Mensagem de status')
with st.status('Preparando dados...', expanded=True) as status:
    st.write('Buscando dados da fonte...')
    time.sleep(2)
    st.write('Processando informações...')
    time.sleep(1)
    st.write('Gerando relatório final...')
    status.update(label='Dados carregados!', state='complete')
st.success('Processo concluído!')

st.download_button(
        label='Baixar dados',
        data='Conteúdo do arquivo',
        file_name='arquivo.txt',
        mime='text/plain'
)