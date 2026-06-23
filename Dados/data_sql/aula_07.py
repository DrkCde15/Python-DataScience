"""
SQLite: Criação do banco de dados da loja.

Cria as tabelas 'cliente', 'marca', 'tel' e 'venda' no banco
loja.db, insere dados de exemplo e faz consultas iniciais.
"""
import sqlite3
import pandas as pd


def ddl():
    """Executa comando DDL (criação/inserção) no banco loja.db."""
    con = sqlite3.connect('./table/loja.db')
    cur = con.cursor()

    consulta = input('Digite o comando SQL: ')
    cur.execute(consulta)

    con.commit()
    con.close()


def dml():
    """Executa consulta SELECT no banco loja.db e exibe como DataFrame."""
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
CREATE TABLE cliente(
    codcliente INT PRIMARY KEY ,
    nome VARCHAR(100),
    cidade VARCHAR(100),
    sexo CHAR(1),
    estado CHAR(2),
    estado_civil CHAR(1)
);
'''
ddl()

'''
CREATE TABLE marca(
    codmarca INT PRIMARY KEY,
    marca VARCHAR(100)
);
'''
ddl()

'''
CREATE TABLE tel(
    codtel INT PRIMARY KEY,
    codmarca INT,
    modelo VARCHAR(100) NOT NULL,
    valor FLOAT,
    FOREIGN KEY(codmarca) REFERENCES modelo(codmarca)
);
'''
ddl()

'''
CREATE TABLE venda(
    codvenda INT PRIMARY KEY,
    codcliente INT,
    codtel INT,
    data_venda DATE,
    FOREIGN KEY(codcliente) REFERENCES cliente(codcliente),
    FOREIGN KEY(codtel) REFERENCES tel(codtel)
);
'''
ddl()

'''
INSERT INTO cliente (codcliente, nome, cidade, sexo, estado, estado_civil) VALUES (1, "Ana Claudia Lima", "Joinville", "F", "SC", "S"), (2, "Joao Silva", "Duque de Caxias", "M", "RJ", "C"), (3, "Maria Santos", "Sao Paulo", "F", "SP", "S"), (4, "Pedro Almeida", "Niteroi", "M", "RJ", "C"), (5, "Lucas Oliveira", "Salvador", "M", "BA", "C"), (6, "Fernanda Costa", "Joao Pessoa", "F", "PB", "S"), (7, "Rafael Santos", "Teresina", "M", "PI", "C"), (8, "Isabela Almeida", "Manaus", "F", "AM", "S");
'''
ddl()

'''
INSERT INTO marca (codmarca, marca) VALUES (1, "Apple"), (2, "Samsung"), (3, "Motorola"), (4, "LG"), (5, "Sony");
'''
ddl()

'''
INSERT INTO tel (codmarca, modelo, codtel, valor) VALUES (1, "Iphone - 15", 1, 2000.00), (2, "M 23", 2, 1500.00), (3, "Moto G", 3, 800.00), (4, "LG - 15", 4, 1000.00), (5, "Xiaomi - 15", 5, 1200.00);
'''
ddl()

'''
INSERT INTO venda (codvenda, codcliente, codtel, data_venda) VALUES (1, 3, 5, "2022-01-01"), (2, 2, 1, "2022-01-02"), (3, 2, 1, "2022-01-03"), (4, 2, 3, "2022-01-04"), (5, 1, 4, "2022-01-05"), (6, 1, 4, "2022-01-06"), (7, 1, 1, "2022-01-07"), (8, 5, 2, "2022-01-08"), (9, 1, 9, "2022-01-09"), (10, 2, 10, "2022-01-10");
'''
ddl()

'''
SELECT * FROM cliente;
'''
dml()

'''
SELECT * FROM marca;
'''
dml()

'''
SELECT * FROM tel;
'''
dml()

'''
SELECT * FROM venda;
'''
dml()