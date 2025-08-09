import sqlite3

# Conecta ao banco
con = sqlite3.connect('./table/test.db')
cur = con.cursor()

# Dados que serão inseridos na tabela
users = [
    ('Ana Lima', 'ana@example.com'),
    ('João Silva', 'joao@example.com'),
    ('Maria Santos', 'maria@example.com'),
    ('Pedro Almeida', 'pedro@example.com'),
    ('Lucas Oliveira', 'lucas@example.com'),
    ('Fernanda Costa', 'fernanda@example.com'),
    ('Rafael Santos', 'rafao@example.com'),
    ('Isabela Almeida', 'isabela@example.com'),
    ('Guilherme Oliveira', 'guilherme@example.com')
]

# Insere dados na tabela
cur.executemany("INSERT INTO users (name, email) VALUES (?, ?)", users)
con.commit()
con.close()