import pandas as pd

#carregando dataset usando o ';' como separador
data =pd.read_csv('./datasets/GasPricesinBrazil_2004-2019.csv', sep=';')

print(data.columns) #imprimindo o nome das colunas
print(data[['DATA INICIAL', 'ESTADO', 'ANO', 'PRODUTO']]) #imprimindo as colunas ESTADO, ANO, PRODUTO e DATA INICIAL