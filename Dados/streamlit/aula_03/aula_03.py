import streamlit as st
import pandas as pd
import numpy as np

st.title('Trabalhando com Dados')

st.header('Gerando e Exibindo dados aleatórios')

df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

# Gerando DataFrames no Streamlit
st.subheader('Data Frame')
st.dataframe(df)

st.subheader('Table')
st.table(df)

# Gerando gráficos
st.subheader('Gráfico de Linhas')
st.line_chart(df) #grafico de linhas

st.subheader('Gráfico de Barras')
st.bar_chart(df) #grafico de barras

st.subheader('Gráfico em Area')
st.area_chart(df) #grafico em area


#Upload de Arquivo
st.subheader('Upload de Arquivo')
upload = st.file_uploader(label='Escolha um arquivo Excel', type='xlsx')
if upload is not None:
    try:
        df_file_upload = pd.read_excel(upload)
        st.success('Arquivo carregado com sucesso')
        st.subheader('As primeiras linhas do arquivo são:')
        st.dataframe(df_file_upload.head())
        
        if df_file_upload.shape[0] > 0:
            st.subheader('Gráfico das primeiras colunas')
            st.line_chart(df_file_upload.iloc[:, :2])
        else:
            st.warning('O arquivo está vazio')
            
    except Exception as e:
        st.error(f'Erro ao carregar o arquivo: {e}')