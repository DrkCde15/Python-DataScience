# SQL - Banco de Dados com SQLite

Scripts para **criação, consulta e manipulação de bancos de dados SQLite** usando Python.

## Estrutura

```
data_sql/
├── aula_01.py          # Criação da tabela users
├── aula_02.py          # Inserção de dados (executemany)
├── aula_03.py          # SELECT + DataFrame pandas
├── aula_04.py          # UPDATE
├── aula_05.py          # DELETE
├── aula_06.py          # Funções DDL/DML genéricas
├── aula_07.py          # Criação do banco loja.db (4 tabelas)
├── aula_08.py          # SELECT básico
├── aula_09.py          # WHERE
├── aula_10.py          # DISTINCT
├── aula_11.py          # ORDER BY (ASC, DESC)
├── aula_12.py          # LIKE (padrões de busca)
├── aula_13.py          # LIMIT
├── aula_14.py          # AND, OR, NOT
├── aula_15.py          # IN
├── aula_16.py          # BETWEEN
└── table/
    ├── loja.db         # Banco da loja (aulas 07-16)
    ├── test.db         # Banco de testes (aulas 01-05)
    └── teste.db        # Banco genérico (aula 06)
```

## Conceitos abordados

- SQLite3 com Python (`sqlite3.connect`, `cursor.execute`)
- DDL: `CREATE TABLE` com constraints
- DML: `INSERT`, `SELECT`, `UPDATE`, `DELETE`
- Cláusulas: `WHERE`, `DISTINCT`, `ORDER BY`, `LIKE`, `LIMIT`, `AND/OR/NOT`, `IN`, `BETWEEN`
- Integração com Pandas (`pd.read_sql_query`)
- Boas práticas: `commit()`, `close()`
