import pandas as pd

#carregando dataset usando o ';' como separador
data =pd.read_csv('./datasets/GasPricesinBrazil_2004-2019.csv', sep=';')

print(data.head(6)) 

avaliacao = pd.DataFrame( #criando um dataframe
    {
        'bom': [50, 21, 100],
        'ruim': [11, 47, 30],
        'muito bom': [35, 49, 86],
        'muito ruim': [1, 5, 10]
    }, index=['playstation', 'xbox', 'nintendo'])
print(avaliacao.iloc[0:2]) #imprimindo as 2 primeiras linhas do dataframe

print(avaliacao.iloc[1, 2]) #imprimindo a linha 0 e a coluna 1 do dataframe

print(avaliacao.iloc[[0, 1]]) #imprimindo as linhas 0 e 1 do dataframe

print(avaliacao.loc['playstation']) #imprimindo a localizacao da linha 0 do dataframe

print(avaliacao.loc[['playstation', 'xbox']]) #imprimindo a localizacao das linhas 0 e 1 do dataframe

print(avaliacao.loc['playstation', 'muito ruim']) #imprimindo a localizacao da linha 0 e a coluna 1 do dataframe

print(data.loc[1:6]) #imprimindo as linhas 1 até 6 do dataframe