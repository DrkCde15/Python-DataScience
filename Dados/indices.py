import pandas as pd

#carregando dataset usando o ';' como separador
data = pd.read_csv('./datasets/GasPricesinBrazil_2004-2019.csv', sep=';')

print(data.index) #imprimindo o index do dataset

avaliacao = pd.DataFrame( #criando um dataframe
    {
        'bom': [50, 21, 100],
        'ruim': [11, 47, 30],
        'muito bom': [35, 49, 86],
        'muito ruim': [1, 5, 10]
    }, index=['playstation', 'xbox', 'nintendo'])
print(avaliacao) #imprimindo o dataframe