import streamlit as st
from utils.load_data import load_data
import plotly.express as px

def data_page():
    st.title("Análise de Dados")

    upload = st.file_uploader(
        "Escolha um arquivo",
        type=["csv", "xlsx", "xls"]
    )

    if upload is not None:
        df = load_data(upload)

        st.success("Arquivo carregado com sucesso!")
        st.dataframe(df)

        colunas_numericas = df.select_dtypes(include=['number']).columns

        if len(colunas_numericas) > 0:
            st.subheader("Gráfico")

            fig = px.bar(
                df,
                y=colunas_numericas[0]
            )

            st.plotly_chart(fig, width='stretch')