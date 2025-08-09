import sqlite3

# Conecta ao banco
con = sqlite3.connect('./table/test.db')
cur = con.cursor()

# Atualiza dados na tabela
cur.execute("UPDATE users SET name = ? WHERE id  = ?", ('Ana Claudia Lima', 1))
con.commit()
con.close()