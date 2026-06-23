"""
Seaborn: Visualização estatística de dados.

Demonstra os principais tipos de gráficos do Seaborn:
dispersão, distribuições, regressão linear e relacionais.
"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# ============================================================
# CARREGAMENTO DOS DADOS
# ============================================================

df = pd.read_excel('./produtos_ficticios.xlsx')
print("Dados carregados:")
print(df)

# ============================================================
# GRÁFICOS DE DISPERSÃO (SCATTERPLOT)
# ============================================================

# Dispersão simples
sns.scatterplot(data=df, x='Preço', y='Nome do produto')

# Com diferenciação por categoria (hue)
sns.scatterplot(data=df, x='Preço', y='Nome do produto', hue='Categoria')

# Com hue + marcadores diferentes (style)
sns.scatterplot(data=df, x='Preço', y='Nome do produto', hue='Categoria', style='Categoria')

# Dispersão por descrição com paleta personalizada
sns.scatterplot(
    data=df, x='Preço', y='Nome do produto',
    hue='Descrição', style='Categoria',
    palette=['red', 'green', 'blue', 'yellow', 'purple']
)
plt.show()

# ============================================================
# GRÁFICO RELACIONAL COM FACETAS (relplot)
# ============================================================

grafico_rel = sns.relplot(
    data=df, x='Preço', y='Nome do produto',
    hue='Categoria', col='Categoria'
)
grafico_rel.set_titles('Categoria: {col_name}')
plt.show()

# ============================================================
# GRÁFICO DE LINHAS (lineplot)
# ============================================================

df_precos = pd.read_excel('./produtos_ficticios.xlsx')
graf_line = sns.lineplot(data=df_precos, x='Preço', y='Categoria', color='red')
plt.show()

# ============================================================
# HISTOGRAMAS E DISTRIBUIÇÕES (displot)
# ============================================================

# Histograma simples
fig = sns.displot(data=df, x='Categoria')

# KDE (funciona apenas com dados numéricos)
sns.displot(data=df, x='Preço', kind='kde')

# Histograma explícito
sns.displot(data=df, x='Categoria', kind='hist')

# ECDF (distribuição acumulada)
sns.displot(data=df, x='Categoria', kind='ecdf')

# Histograma com rug e facetas por categoria
sns.displot(data=df, x='Categoria', hue='Descrição', col='Categoria', rug=True)
plt.show()

# ============================================================
# REGRESSÃO LINEAR
# ============================================================

# Regressão simples
sns.regplot(data=df, x='Preço', y='Quantidade em estoque')

# Regressão com facetas por categoria
sns.lmplot(
    data=df, x='Preço', y='Quantidade em estoque',
    hue='Categoria', col='Categoria',
    palette=['red', 'green', 'blue'],
    markers=['o', 'v', 'x']
)
plt.show()