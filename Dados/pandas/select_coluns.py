import pandas as pd

#carregando dataset usando o ';' como separador
data =pd.read_csv('./datasets/GasPricesinBrazil_2004-2019.csv', sep=';')
print(data.head(5))

print(data[['DATA INICIAL', 'ESTADO', 'ANO', 'PRODUTO']]) #imprimindo a coluna ESTADO, ANO, PRODUTO e DATA INICIAL
print(list(data.columns)) #imprimindo o nome das colunas