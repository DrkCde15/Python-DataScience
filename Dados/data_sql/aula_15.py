# IN

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
SELECT * FROM cliente WHERE cidade IN ('Rio de Janeiro', 'Niteroi');
'''
dml()

'''
SELECT * FROM tel WHERE valor IN (800.0, 1000.0, 1200.0);
'''
dml()