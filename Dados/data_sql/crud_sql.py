import sqlite3
import os

DB_PATH = './table/test.db'
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

def criar_tabela():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
    """)
    con.commit()
    con.close()

def inserir_usuario():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    nome = input("Digite o nome: ")
    email = input("Digite o email: ")

    cur.execute("SELECT * FROM users WHERE email = ?", (email,))
    if cur.fetchone():
        print("Já existe um usuário com esse email.")
    else:
        try:
            cur.execute("INSERT INTO users (username, email) VALUES (?, ?)", (nome, email))
            con.commit()
            print("Usuário inserido com sucesso!")
        except sqlite3.IntegrityError:
            print("Falha ao inserir. Email já existente.")
    
    con.close()

def atualizar_usuario():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    email_busca = input("Digite o email do usuário que deseja atualizar: ")
    cur.execute("SELECT * FROM users WHERE email = ?", (email_busca,))
    usuario = cur.fetchone()

    if usuario:
        print(f"Usuário encontrado: ID={usuario[0]}, Nome={usuario[1]}, Email={usuario[2]}")
        novo_nome = input("Novo nome (Enter para manter): ") or usuario[1]
        novo_email = input("Novo email (Enter para manter): ") or usuario[2]

        try:
            cur.execute("UPDATE users SET username = ?, email = ? WHERE email = ?", (novo_nome, novo_email, email_busca))
            con.commit()
            print("Usuário atualizado com sucesso!")
        except sqlite3.IntegrityError:
            print("Este novo email já está em uso por outro usuário.")
    else:
        print("Usuário não encontrado.")
    
    con.close()

def remover_usuario():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    email = input("Digite o email do usuário que deseja remover: ")
    cur.execute("SELECT * FROM users WHERE email = ?", (email,))
    usuario = cur.fetchone()

    if usuario:
        print(f"Usuário encontrado: ID={usuario[0]}, Nome={usuario[1]}, Email={usuario[2]}")
        confirmar = input("Tem certeza que deseja remover? (s/n): ").lower()
        if confirmar == 's':
            cur.execute("DELETE FROM users WHERE email = ?", (email,))
            con.commit()
            print("Usuário removido com sucesso!")
        else:
            print("Remoção cancelada.")
    else:
        print("Usuário não encontrado.")
    
    con.close()

def listar_usuarios():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("SELECT id, username, email FROM users")
    usuarios = cur.fetchall()

    if usuarios:
        print("\nLista de Usuários:")
        for id, nome, email in usuarios:
            print(f"ID: {id} | Nome: {nome} | Email: {email}")
    else:
        print("Nenhum usuário cadastrado.")
    
    con.close()

def menu():
    criar_tabela()
    while True:
        print("\n===== MENU =====")
        print("1 - Inserir usuário")
        print("2 - Atualizar usuário")
        print("3 - Remover usuário")
        print("4 - Listar usuários")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            inserir_usuario()
        elif opcao == '2':
            atualizar_usuario()
        elif opcao == '3':
            remover_usuario()
        elif opcao == '4':
            listar_usuarios()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
