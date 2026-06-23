"""
SQLite: Cláusula DISTINCT.

Demonstra como selecionar valores únicos de colunas
para eliminar duplicatas nos resultados.
"""
import sqlite3
import pandas as pd


def dml():
    """Executa SELECT DISTINCT e exibe como DataFrame."""
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
SELECT DISTINCT estado FROM cliente;
'''
dml()

'''
SELECT DISTINCT cidade FROM cliente;
'''
dml()