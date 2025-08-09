def ddl():
    import sqlite3
    
    # Conecta ao banco
    banco = input('Digite o nome do banco: ')
    con = sqlite3.connect(banco)
    cur = con.cursor()

    # Cria a tabela
    consulta = input('Digite o comando SQL: ')
    cur.execute(consulta)
    
    # Insere dados na tabela
    con.commit()
    con.close

def dml():
    import sqlite3
    import pandas as pd
    
    banco = input('Digite o nome do banco: ')
    con = sqlite3.connect(banco)
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
CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT NOT NULL UNIQUE)
'''
ddl()

'''INSERT INTO users (name, email) VALUES ("Joao silva", "joao.silva@example.com")
'''
ddl()

'''SELECT * FROM users'''
dml()