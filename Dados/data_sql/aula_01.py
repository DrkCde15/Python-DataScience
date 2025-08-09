import sqlite3

# Conecta ao banco
con = sqlite3.connect('./table/test.db')
cur = con.cursor()

# Cria a tabela
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
""")
# Insere dados na tabela
con.commit()
con.close()