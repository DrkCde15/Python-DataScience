import pandas as pd

#carregando dataset usando o ';' como separador
data =pd.read_csv('./datasets/GasPricesinBrazil_2004-2019.csv', sep=';')

print(data.head(6))

print(data.iloc[1]) #imprimindo a linha 1 do dataframe

print(data.iloc[:6]) #imprimindo as 6 primeiras linhas do dataframe

print(data.iloc[20:24]) #imprimindo as 4 linhas da região Sudeste do dataframe

print(data.iloc[[5, 10, 15, 20]]) #imprimindo as linhas 5, 10, 15 e 20 do dataframe

print(data.iloc[1, 4]) #imprimindo a linha 1 e a coluna 4 do dataframe