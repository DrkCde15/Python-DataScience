import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('./produtos_ficticios.xlsx')
print (df)

# Gráfico de Dispersão
sns.scatterplot(data=df, x='Preço', y='Nome do produto')
sns.scatterplot(data=df, x='Preço', y='Nome do produto', hue='Categoria')
sns.scatterplot(data=df, x='Preço', y='Nome do produto', hue='Categoria', style='Categoria')
sns.scatterplot(data=df, x='Preço', y='Nome do produto', hue='Descrição', style='Categoria')
sns.scatterplot(data=df, x='Preço', y='Nome do produto', hue='Descrição', style='Categoria', palette= ['red', 'green', 'blue', 'yellow', 'purple'])
plt.show()

# Gráfico de Dispersão Relacional
grafico_rel = sns.relplot(data=df, x='Preço', y='Nome do produto', hue='Categoria', col='Categoria')
grafico_rel.set_titles('Este grafico representa a Categoria de {col_name}')
plt.show()

# Gráfico de linhas
df_precos = pd.read_excel('./produtos_ficticios.xlsx')
print(df_precos[['Preço', 'Categoria']]) #imprimindo as colunas Preço e Categoria
graf_line = sns.lineplot(data=df_precos, x='Preço', y='Categoria', color = 'red')
plt.show()

# Histogramas
fig = sns.displot(data=df, x='Categoria')
fig = sns.displot(data=df, x='Preço', kind='kde') # kde fuciona apenas com dados numericos
fig = sns.displot(data=df, x='Categoria', kind='hist')
fig = sns.displot(data=df, x='Categoria', kind='ecdf')
fig = sns.displot(data=df, x='Categoria', hue='Descrição', col='Categoria', rug=True)
plt.show()

# Regreção linear
sns.regplot(data=df, x='Preço', y='Quantidade em estoque')
sns.lmplot(data=df, x='Preço', y='Quantidade em estoque', hue='Categoria', palette= ['red', 'green', 'blue'], col='Categoria', markers=['o', 'v', 'x'])
plt.show()