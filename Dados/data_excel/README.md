# Excel - Criação e Manipulação de Planilhas

Scripts para **criação, formatação e manipulação de arquivos Excel (.xlsx)** usando OpenPyXL e Pandas.

## Arquivos

| Arquivo | Descrição |
|---------|-----------|
| `criacao.py` | Cria uma planilha do zero com 50 produtos aleatórios (nomes, quantidades, preços) |
| `formulas.py` | Adiciona colunas com fórmulas (Preço de venda, Total, Lucro) usando referências de células |
| `graficos.py` | Insere gráficos de barras, linhas e pizza na planilha usando OpenPyXL |
| `read.py` | Leitura e exibição de dados de arquivo Excel com Pandas |

## Conceitos abordados

- `openpyxl.Workbook()` e `load_workbook()`
- Inserção de dados e fórmulas em células
- `openpyxl.chart` (BarChart, LineChart, PieChart)
- Leitura com `pd.read_excel()`
- Referências absolutas e relativas em fórmulas
