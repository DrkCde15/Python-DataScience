"""
SQLite: Funções genéricas DDL e DML.

Fornece funções reutilizáveis para executar comandos SQL
(DDL para criação/alteração, DML para consultas) e exibir
resultados como DataFrame do pandas.
"""
import sqlite3
import pandas as pd


def ddl():
    """
    Executa um comando DDL (Data Definition Language).
    Útil para CREATE, ALTER, DROP, INSERT, UPDATE, DELETE.
    Pede o nome do banco e o comando SQL via input().
    """
    banco = input('Digite o nome do banco (ex: teste.db): ')
    con = sqlite3.connect(banco)
    cur = con.cursor()

    consulta = input('Digite o comando SQL: ')
    cur.execute(consulta)

    con.commit()
    con.close()


def dml():
    """
    Executa uma consulta DML (Data Manipulation Language).
    Útil para SELECT. Exibe o resultado como DataFrame do pandas.
    """
    banco = input('Digite o nome do banco (ex: teste.db): ')
    con = sqlite3.connect(banco)
    cur = con.cursor()

    query = input('Digite a Query desejada: ')
    cur.execute(query)

    registros = cur.fetchall()
    colunas = [desc[0] for desc in cur.description]

    df = pd.DataFrame(registros, columns=colunas)
    print(df)

    con.close()


# ============================================================
# EXEMPLOS DE USO (descomente para executar)
# ============================================================

# Criação da tabela users
# ddl()  -- digite: CREATE TABLE IF NOT EXISTS users (...)

# Inserção de dados
# ddl()  -- digite: INSERT INTO users (...)

# Consulta
# dml()  -- digite: SELECT * FROM users