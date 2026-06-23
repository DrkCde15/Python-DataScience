"""
SQLite: Comando SELECT básico.

Demonstra consultas SELECT para listar dados de todas as tabelas
do banco loja.db, incluindo seleção de colunas específicas.
"""
import sqlite3
import pandas as pd


def dml():
    """Executa consulta SELECT e exibe resultado como DataFrame."""
    con = sqlite3.connect('./table/loja.db')
    cur = con.cursor()

    query = input('Digite a Query desejada: ')
    cur.execute(query)

    registros = cur.fetchall()
    colunas = [desc[0] for desc in cur.description]

    df = pd.DataFrame(registros, columns=colunas)
    print(df)

    con.close()
    
'''
SELECT * FROM cliente;
'''
dml()

'''
SELECT * FROM marca;
'''
dml()

'''
SELECT * FROM tel;
'''
dml()

'''
SELECT * FROM venda;
'''
dml()

'''
SELECT nome FROM cliente;
'''
dml()

'''
SELECT modelo FROM tel;
'''
dml()

'''
SELECT nome, cidade, estado FROM cliente;
'''
dml()