# PySpark - Aulas Práticas

Bem-vindos a pasta **pyspark** do repositório de Python Data Science. Aqui você encontrará aulas práticas de **PySpark** para manipulação, leitura e escrita de dados em diferentes formatos.

---

## Estrutura da Pasta

```
pyspark/
├── datasets/
│   ├── marca_carro.csv        # Cadastro de marcas de carros (56 registros)
│   ├── modelo_carro.csv       # Modelos de carros com preço (1000 registros)
│   └── marcas_duplicadas.csv  # Lista de marcas duplicadas para exercícios
├── Aula 1 - PySpark.ipynb     # Carregamento e escrita de dados
├── Aula 2 - PySpark.ipynb     # Leitura e conversão de formatos
├── Aula 3 - PySpark.ipynb     # Seleção de colunas (Select)
├── Aula 4 - PySpark.ipynb     # Filtros (Where)
├── Aula 5 - PySpark.ipynb     # Remoção de duplicados
├── Aula 6 - PySpark.ipynb     # Tipagem de dados (Cast)
├── Aula 7 - PySpark.ipynb     # Like e Between
├── Aula 8 - PySpark.ipynb     # Substring, Left e Right
├── Aula 9 - PySpark.ipynb     # JOINS (Inner, Left, Right)
├── Aula 10 - PySpark.ipynb    # Exists e Left Semi Join
└── README.md
```

---

## Conteúdo das Aulas

### Aula 1 - PySpark: Carregamento
- Leitura de arquivos CSV com `spark.read.format('csv')`
- Exibição de DataFrames com `display()`
- Escrita de dados em CSV com modos `overwrite` e `append`
- Contagem de registros com `count()`

### Aula 2 - PySpark: Leitura e Conversão de Formatos
- Leitura de CSV com opções de `header`, `encoding` e `sep`
- Conversão e escrita em múltiplos formatos: **Parquet**, **JSON** e **Avro**
- Leitura de arquivos JSON com `spark.read.format('json')`

### Aula 3 - PySpark: Select
- Seleção de colunas específicas com `select()`
- Criação de Views temporárias com `createOrReplaceTempView()`
- Uso de SQL no Spark para manipulação de dados
- Renomeação de colunas com `selectExpr()`

### Aula 4 - PySpark: Filtros
- Aplicação de filtros em DataFrames com `where()`
- Condições de filtragem usando `col()` com operadores `|` (OR) e `&` (AND)
- Filtros SQL usando views temporárias
- Acesso a colunas por DataFrame (`df['col']`) ou atributo (`df.col`)

### Aula 5 - PySpark: Removendo Duplicados
- Identificação de registros duplicados
- Remoção de duplicatas com `distinct()` e `dropDuplicates()`
- Normalização de dados com `regexp_replace()` para limpeza de valores

### Aula 6 - PySpark: Tipagem de Dados
- Conversão de tipos com `cast()` (INT, DOUBLE, STRING)
- Uso de `withColumn()` para alterar tipos de colunas
- Exibição de schema com `printSchema()`
- Conversão de tipos via SQL com `CAST`

### Aula 7 - PySpark: Like e Between
- Filtros de texto com `LIKE` (começa com, termina com, contém)
- Filtros de intervalo com `BETWEEN`
- Combinação de filtros LIKE e BETWEEN
- Uso das funções `like()` e `between()` na API PySpark

### Aula 8 - PySpark: Substring, Left e Right
- Extração de substrings com `substring()`
- Funções `left()` e `right()` para extração de caracteres
- Uso de `expr()` para funções SQL no PySpark
- Combinação de múltiplas funções de string

### Aula 9 - PySpark: JOINS
- **INNER JOIN**: Retorna registros com correspondência em ambas as tabelas
- **LEFT JOIN**: Retorna todos os registros da tabela esquerda
- **RIGHT JOIN**: Retorna todos os registros da tabela direita
- Uso de `join()` na API PySpark com diferentes tipos

### Aula 10 - PySpark: Exists e Left Semi
- Subquery `EXISTS` para verificar existência de registros
- **LEFT SEMI JOIN**: Equivalente ao EXISTS no PySpark
- Comparação entre abordagens SQL e API PySpark

---

## Datasets

| Arquivo              | Descrição                                | Registros |
|----------------------|------------------------------------------|-----------|
| `marca_carro.csv`    | Código e nome das marcas de carros       | 56        |
| `modelo_carro.csv`   | Modelos, preços e código da marca        | 1000      |
| `marcas_duplicadas.csv` | Lista com marcas duplicadas          | 1000      |

---

## Ferramentas e Tecnologias

<div align="center">
  <table>
    <tr>
      <td align="center" width="96">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" width="48" height="48" alt="Python" />
        <br>Python
      </td>
      <td align="center" width="96">
        <img src="https://spark.apache.org/images/spark-logo-rev.svg" width="48" height="48" alt="PySpark" />
        <br>PySpark
      </td>
      <td align="center" width="96">
        <img src="https://databricks.com/wp-content/uploads/2021/04/databricks-logo.png" width="48" height="48" alt="Databricks" />
        <br>Databricks
      </td>
    </tr>
  </table>
</div>

---

## Aprendizados

- Leitura e escrita de dados com PySpark
- Trabalhar com os formatos CSV, Parquet, JSON e Avro
- Uso de modos de escrita (`overwrite`, `append`)
- Seleção de colunas com `select()` e `selectExpr()`
- Criação de Views temporárias e uso de SQL
- Filtros com `where()`, `like()` e `between()`
- Remoção de duplicatas com `distinct()` e `dropDuplicates()`
- Conversão de tipos de dados com `cast()`
- Funções de string: `substring()`, `left()`, `right()`
- Operações de JOIN: INNER, LEFT, RIGHT e LEFT SEMI
- Manipulação básica de DataFrames no Databricks

---

## Contatos

<div>
<a href="https://mail.google.com/mail/u/1/#inbox"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"></a>
<a href="https://www.linkedin.com/in/julio-santana-ads/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a>
</div>
