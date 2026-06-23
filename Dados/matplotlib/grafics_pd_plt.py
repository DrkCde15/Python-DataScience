"""
Matplotlib + Pandas: Visualização de séries temporais.

Carrega dados de índice financeiro (CSV), filtra apenas o índice NYA
e cria 3 subplots (linha, barras, dispersão) lado a lado.
"""
import matplotlib.pyplot as plt
import pandas as pd

# ============================================================
# CARREGAMENTO E FILTRAGEM DOS DADOS
# ============================================================

df = pd.read_csv('./indexData.csv', sep=',')

# Seleciona apenas as colunas de interesse
df_1 = df[['Index', 'Date', 'Close']]

# Remove linhas que NÃO são do índice NYA
df_rm = df_1.loc[(df_1['Index'] != 'NYA')]
df_final = df_1.drop(df_rm.index)

# Pega apenas os dados mais recentes (a partir da linha 13900)
df_final = df_final[13900:]

# ============================================================
# CRIAÇÃO DE SUBPLOTS (1 linha, 3 colunas)
# ============================================================

fig = plt.figure(figsize=(20, 4))

# ---- Gráfico 1: Linha ----
fig.add_subplot(131)
plt.plot(df_final['Date'], df_final['Close'], label='NYA', color='m', ls='--', lw=2.0)
plt.legend(loc=2)
plt.ylabel('Fechamento')
plt.xlabel('Data')
plt.title('Gráfico Linha')
plt.tight_layout()

# ---- Gráfico 2: Barras ----
fig.add_subplot(132)
plt.bar(df_final['Date'], df_final['Close'], label='NYA', color='b', lw=2.0)
plt.legend(loc=1)
plt.ylabel('Fechamento')
plt.xlabel('Data')
plt.title('Gráfico Barras')
plt.tight_layout()

# ---- Gráfico 3: Dispersão ----
fig.add_subplot(133)
plt.scatter(df_final['Date'], df_final['Close'], label='NYA', color='r', lw=2.0)
plt.legend(loc=1)
plt.ylabel('Fechamento')
plt.xlabel('Data')
plt.title('Gráfico Pontos')
plt.tight_layout()

# ============================================================
# EXPORTAÇÃO E EXIBIÇÃO
# ============================================================

plt.savefig('./figs/data_close.png')
plt.show()