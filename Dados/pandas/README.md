# Pandas - Manipulação e Análise de Dados

Scripts para **manipulação, análise e visualização de dados** usando o Pandas. Baseado no dataset de preços de combustíveis no Brasil (`GasPricesinBrazil_2004-2019.csv`).

## Arquivos

| Arquivo | Descrição |
|---------|-----------|
| `series.py` | Criação e manipulação de Series; acesso a colunas como Series |
| `criando_dtfrm.py` | Criação de DataFrames a partir de dicionários; renomeação de colunas |
| `carregando_dados.py` | Leitura de CSV com encoding `latin1` e separador `;` |
| `manip_dados.py` | Exploração inicial: `head()`, `info()`, `shape`, `type()` |
| `titles_coluns.py` | Exibição e seleção de nomes de colunas |
| `select_coluns.py` | Seleção de colunas específicas por lista de nomes |
| `indices.py` | Visualização do índice padrão; criação de índices personalizados |
| `indices_selection.py` | Indexação por posição com `iloc` |
| `labels.py` | Indexação por rótulo com `loc` vs `iloc` |
| `filtragem_dts.py` | Filtros booleanos, `query()`, operadores `&`, `\|`, `!=` |
| `atribuindo_dados.py` | Atribuição de valores, cópia de colunas, criação de listas |
| `nw_coluns.py` | Adição e remoção de colunas |
| `agregacao.py` | Agrupamento com `groupby()` e agregações (`sum`, `mean`, `max`) |
| `save_dtset.py` | Salvamento de DataFrame modificado para CSV |

## Dataset

Os scripts utilizam o dataset público **GasPricesinBrazil_2004-2019.csv** com preços de combustíveis por estado brasileiro.
