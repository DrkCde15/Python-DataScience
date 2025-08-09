import sqlite3
import pandas as pd

# Conecta ao banco
con = sqlite3.connect('./table/test.db')
cur = con.cursor()

# Seleciona todos os clientes
cur.execute("SELECT * FROM users")
users = cur.fetchall() # retorna uma tupla

# seleciona os nomes das colunas
coluns = [desc[0] for desc in cur.description]

# cria um dataframe a partir da tupla e das colunas
df_clientes = pd.DataFrame(users, columns=coluns)
print(df_clientes)

con.close()