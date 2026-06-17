import sqlite3 as sql
import streamlit as st
import pandas as pd
import requests as req


st.title('Integração com BD e APIs')

# Criar e conectar com o BD sqlite
conn = sql.connect('banco.db')
cur = conn.cursor()

# Criação de tabelas
cur.execute("""
CREATE TABLE IF NOT EXISTS produtos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    quantidade INT,
    preco REAL NOT NULL
)
""")

# Inserindo dados
cur.execute(
    "INSERT INTO produtos (nome, quantidade, preco) VALUES ('PC', 3000, 10000.00)"
    )

cur.execute(
    "INSERT INTO produtos (nome, quantidade, preco) VALUES ('Mouse', 10000, 20.00)"
    )

conn.commit()

st.header('Produtos')

# Buscando dados e mostrando em um DataFrame
query = 'SELECT * FROM produtos'
df_prod = pd.read_sql_query(query, conn)
st.dataframe(df_prod)

conn.commit()
conn.close()

# Busca em API
st.header('Busca em API')
try:
    # --- Obter a requisição --- #
    resposta = req.get('https://jsonplaceholder.typicode.com/posts?_limit=5')
    posts = resposta.json()

    # --- Mostrar as informações no site --- #
    for post in posts:
        st.subheader(post['title'])
        st.write(post['body'])
        st.write('---')
except req.exceptions.RequestException as e:
    # --- Caso ocorra algum erro de cnoxão, mostrar qual foi o erro --- #
    st.error(f'Erro ao acessar a API: {e}')