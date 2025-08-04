import pandas as pd

df = pd.read_excel('./estoque.xlsx')
pd.set_option('display.max_columns', None) # mostra todas as colunas

print(df.head(54))  # mostra todas as linhas
