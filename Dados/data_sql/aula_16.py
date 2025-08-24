# BETWEEN

def dml():
    import sqlite3
    import pandas as pd
    
    # Conecta ao banco
    con = sqlite3.connect('./table/loja.db')
    cur = con.cursor()
    
    query = input('Digite a Query desejada: ')
    cur.execute(query)
    
    users = cur.fetchall() # retorna uma tupla

    # seleciona os nomes das colunas
    coluns = [desc[0] for desc in cur.description]

    # cria um dataframe a partir da tupla e das colunas
    df_clientes = pd.DataFrame(users, columns=coluns)
    print(df_clientes)

    con.close
    
'''
SELECT modelo, valor FROM tel WHERE valor BETWEEN 1000.0 AND 2000.0
'''
dml()