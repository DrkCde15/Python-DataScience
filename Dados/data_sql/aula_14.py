"""
SQLite: Operadores lógicos AND, OR, NOT.

Demonstra combinação de múltiplas condições em consultas
para filtrar registros de forma mais precisa.
"""
import sqlite3
import pandas as pd


def dml():
    """Executa SELECT com operadores lógicos e exibe como DataFrame."""
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
SELECT * FROM cliente WHERE estado_civil = 'S' OR cidade = 'Sao Paulo';
'''
dml()

'''
SELECT * FROM cliente WHERE sexo = 'M' AND estado = 'RJ';
'''
dml()

'''
SELECT * FROM cliente WHERE NOT sexo = 'F';
'''
dml()