import pandas as pd

#carregando dataset usando o ';' como separador
data =pd.read_csv('./datasets/GasPricesinBrazil_2004-2019.csv', sep=';')

new_colun = data['COLUNM'] = "New Dataset" #criando uma nova coluna e atribuindo um valor
print(new_colun) #mostrando a nova coluna
print(data.head(6))

new_colun2 = data['COLUNM_2'] = range(data.shape[0]) #criando uma nova coluna e atribuindo um valor de acordo com o numero de linhas
print(new_colun2) #mostrando a nova coluna
print(data.head(6))

new_colun3 = data['COLUNM_3'] = data['PREÇO MÉDIO REVENDA'] * 6.3 #criando uma nova coluna e atribuindo um valor de acordo com a coluna PREÇO MÉDIO REVENDA
print(new_colun3)
print(data.head(6))

print(data.copy("new_colun3")) #criando uma copia das colunas

del data['Unnamed: 0'] #deletando a coluna Unnamed: 0
del data['COLUNM'] #deletando a coluna COLUNM
del data['COLUNM_2'] #deletando a coluna COLUNM
del data['COLUNM_3'] #deletando a coluna COLUNM
print(data.head(6))