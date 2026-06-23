"""
Pandas: Trabalhando com Series.

Demonstra acesso a colunas como Series e criação
de Series personalizadas com índices e nomes.
"""
import pandas as pd

# ============================================================
# ACESSO A COLUNAS COMO SERIES
# ============================================================

data = pd.read_csv('./datasets/GasPricesinBrazil_2004-2019.csv', sep=';')

# Acessando uma coluna como Series (duas formas equivalentes)
print("Coluna ESTADO (notação dict):")
print(data['ESTADO'])
print("\nColuna ESTADO (notação atributo):")
print(data.ESTADO)

# Acessando uma linha inteira como Series via índice posicional
print("\nLinha 4 (iloc):")
print(data.iloc[4])

# ============================================================
# CRIAÇÃO DE SERIES A PARTIR DE LISTAS
# ============================================================

# Series com strings
print("\nSeries de strings:")
print(pd.Series(['a', 'b', 'c']))

# Series com inteiros
print("\nSeries de inteiros:")
print(pd.Series([1, 2, 3]))

# Series com floats
print("\nSeries de floats:")
print(pd.Series([5.5, 6.0, 3.9]))

# Series com índice personalizado e nome
print("\nSeries com índice e nome:")
print(pd.Series([5.5, 6.0, 3.9], index=['P1', 'P2', 'P3'], name='Provas'))