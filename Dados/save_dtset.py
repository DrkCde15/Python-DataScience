import pandas as pd

#carregando dataset usando o ';' como separador
data =pd.read_csv('./datasets/GasPricesinBrazil_2004-2019.csv', sep=';')
print(data.head(5))

new_colun = data['COLUNM'] = "Gostosa" #criando uma nova coluna e atribuindo um valor
print(new_colun) #mostrando a nova coluna
print(data.head(6))

del data['Unnamed: 0'] #deletando a primeira coluna
print(data.head(6))
print(list(data.columns)) #imprimindo o nome das colunas

data.to_csv('./datasets/GasPricesinBrazil_2004-2019_new.csv', sep=';', index=False)