import sqlite3

# Conecta ao banco
con = sqlite3.connect('./table/test.db')
cur = con.cursor()

# Deleta dados na tabela
cur.execute("DELETE FROM users WHERE id = ?", (1,))
con.commit()
con.close()