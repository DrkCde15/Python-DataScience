# --- Importar as bibliotecas --- #
import numpy as np
import pandas as pd
import streamlit as st

# --- Configuração da página --- #
st.set_page_config(layout='wide')

# --- Título da página --- #
st.title('Aula de st.tabs()')

# --- Criar as abas --- #
abas = st.tabs(['Gráficos', 'Formulário', 'Dados'])

# --- Trabalhar com as abas --- #
with abas[0]:
    st.header('Visualização com Gráficos')

    dados_linha = pd.DataFrame({
        'Semana': ['S1', 'S2', 'S3', 'S4', 'S5'],
        'Vendas': [10, 12, 8, 15, 18]
    }).set_index('Semana')

    st.subheader('Gráfico de linha')
    st.line_chart(dados_linha)

    dados_barra = pd.DataFrame({
        'Produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor'],
        'Preço': [4500, 120, 250, 900],
        'Vendas': [25, 40, 30, 20]
    }).set_index('Produto')

    st.subheader('Gráfico de barras')
    st.bar_chart(dados_barra)

    dados_area = pd.DataFrame(
        np.random.rand(20, 3),
        columns=['Canal A', 'Canal B', 'Canal C']
    )

    st.subheader('Gráfico de área')
    st.area_chart(dados_area)

with abas[1]:
    st.header('Cadastro')
    st.write('Formulário básico dentro de uma aba')

    with st.form('formulario_usuario'):
        nome = st.text_input('Nome:')
        email = st.text_input('E-mail:')
        idade = st.number_input('Idade', min_value=0, max_value=1000)
        enviar = st.form_submit_button('Enviar')

    if enviar:
        st.success('Dados enviados com sucesso!')
        st.header('Dados do cliente:')
        st.subheader(f'Nome: {nome}')
        st.subheader(f'E-mail: {email}')
        st.subheader(f'Idade: {idade}')

with abas[2]:
    st.header('Visualização de dados')
    st.write('Tabela e filtros simples')

    dados = {
        'Produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor'],
        'Preço': [4500, 120, 250, 900],
        'Estoque': [10, 50, 30, 20]
    }

    filtro_preco = st.slider('Preço máximo:', 0, 5000, 5000)

    dados_filtrados = {
        c: [v[i] for i in range(len(dados['Preço'])) if dados['Preço'][i] <= filtro_preco]
        for c, v in dados.items()
    }

    st.dataframe(dados_filtrados)