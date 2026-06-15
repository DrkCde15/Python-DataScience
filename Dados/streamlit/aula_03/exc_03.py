import streamlit as st
import pandas as pd

st.title('Análise de Arquivos')

st.header('Gerando e Exibindo dados de um arquivo')

file_types = ['csv', 'xlsx', 'xls']

st.subheader('Upload de Arquivo')
upload = st.file_uploader(
    label='Escolha um arquivo',
    type=file_types
)

if upload is not None:
    try:
        # Obtém a extensão do arquivo
        extension = upload.name.split('.')[-1].lower()

        # Lê o arquivo de acordo com o tipo
        if extension == 'csv':
            df_file_upload = pd.read_csv(upload, sep=None, engine='python')

        elif extension in ['xlsx', 'xls']:
            df_file_upload = pd.read_excel(upload)

        else:
            st.error('Tipo de arquivo não suportado.')
            st.stop()

        st.success('Arquivo carregado com sucesso!')

        st.subheader('As primeiras linhas do arquivo são:')
        st.dataframe(df_file_upload.head())

        if df_file_upload.shape[0] > 0:
            st.subheader('Gráfico das primeiras colunas numéricas')

            # Seleciona apenas colunas numéricas
            numeric_columns = df_file_upload.select_dtypes(
                include=['number']
            )

            if numeric_columns.shape[1] >= 2:
                st.line_chart(numeric_columns.iloc[:, :2])
            else:
                st.warning(
                    'O arquivo não possui pelo menos duas colunas numéricas para gerar o gráfico.'
                )

        else:
            st.warning('O arquivo está vazio.')

    except Exception as e:
        st.error(f'Erro ao carregar o arquivo: {e}')