"""
Pandas: Filtragem e seleção condicional de dados.

Demonstra diferentes técnicas de filtragem:
  - Máscaras booleanas
  - .loc e .query()
  - Operadores & (AND), | (OR), != (XOR)
  - Filtros encadeados
  - Reset de índice após filtragem
"""
import pandas as pd

# ============================================================
# CARREGAMENTO E VISUALIZAÇÃO INICIAL
# ============================================================

data = pd.read_csv('./datasets/GasPricesinBrazil_2004-2019.csv', sep=';')
print("Primeiras 6 linhas:")
print(data.head(6))

# ============================================================
# FILTRAGEM COM MÁSCARAS BOOLEANAS
# ============================================================

print("\nEstados únicos no dataset:")
print(data['ESTADO'].unique())

# Máscara booleana: comparação elemento a elemento
selecao = data['ESTADO'] == 'SAO PAULO'
print(f"\nTipo da máscara: {type(selecao)}")
print(f"Shape da máscara: {selecao.shape}")
print(f"Shape do dataset: {data.shape}")

# Aplicando a máscara ao DataFrame
print("\nPostos de SAO PAULO (notação direta):")
print(data[selecao])

# Usando .loc para filtragem baseada em rótulo
print("\nPostos de SAO PAULO (.loc):")
print(data.loc[selecao])

# Usando .query() - sintaxe mais legível para filtros
print("\nPostos de SAO PAULO (.query):")
print(data.query('ESTADO == "SAO PAULO"'))

# ============================================================
# RESET DE ÍNDICE APÓS FILTRAGEM
# ============================================================

postos_sp = data.query('ESTADO == "SAO PAULO"')

# Reset mantendo o índice original como coluna
print("\nReset com índice original:")
print(postos_sp.reset_index())

# Reset descartando o índice original
print("\nReset sem índice original:")
print(postos_sp.reset_index(drop=True))

# Reset inplace (modifica o próprio DataFrame)
postos_sp.reset_index(drop=True, inplace=True)
print("\nApós reset inplace:")
print(postos_sp)

# ============================================================
# FILTROS COM OPERADORES LÓGICOS
# ============================================================

# AND (&): ambas as condições devem ser verdadeiras
selecao = (data['ESTADO'] == 'RIO DE JANEIRO') & (data['PREÇO MÉDIO REVENDA'] > 2.0)
print("\nRIO DE JANEIRO com preço > 2.0 (AND):")
print(data[selecao])

# OR (|): pelo menos uma condição verdadeira
selecao = (data['ESTADO'] == 'RIO DE JANEIRO') | (data['PREÇO MÉDIO REVENDA'] > 2.0)
print("\nRIO DE JANEIRO OU preço > 2.0 (OR):")
print(data[selecao])

# XOR (!=): uma condição verdadeira e a outra falsa
selecao = (data['ESTADO'] == 'RIO DE JANEIRO') != (data['PREÇO MÉDIO REVENDA'] > 2.0)
print("\nXOR entre estado=RJ e preço>2.0:")
print(data[selecao])

# ============================================================
# FILTROS ENCADEADOS
# ============================================================

select_1 = (data['ESTADO'] == 'RIO DE JANEIRO')
df_rj = data[select_1]

select_2 = df_rj['PREÇO MÉDIO REVENDA'] > 2.0
df_rj_preco = df_rj[select_2]
print("\nFiltro encadeado (RJ com preço > 2.0):")
print(df_rj_preco)

# ============================================================
# FILTROS COMBINADOS (MÚLTIPLAS CONDIÇÕES)
# ============================================================

selecao_estados = (data['ESTADO'] == 'RIO DE JANEIRO') | (data['ESTADO'] == 'SAO PAULO')
selecao_produto = (data['PRODUTO'] == 'GASOLINA COMUM')
selecao_preco = (data['PREÇO MÉDIO REVENDA'] > 2.0)

# Combinação de 3 condições com AND
select_final = selecao_estados & selecao_produto & selecao_preco
print("\nGasolina comum em RJ/SP com preço > 2.0:")
print(data[select_final])

# Combinação direta em uma única expressão
select = ((data['ESTADO'] == 'RIO DE JANEIRO') | (data['ESTADO'] == 'SAO PAULO'])
          & (data['PRODUTO'] == 'GASOLINA COMUM')
          & (data['PREÇO MÉDIO REVENDA'] > 2.0))
print("\nMesmo filtro em expressão única:")
print(data[select])