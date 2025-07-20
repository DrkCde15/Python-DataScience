import pandas as pd

#carregando dataset usando o ';' como separador
data =pd.read_csv('./datasets/GasPricesinBrazil_2004-2019.csv', sep=';')
print(data)

#selecionando 5 primeiras linhas
print(data.head(5))

#exibe informacoes sobre o dataset
print(data.info())

#tipo de variável
print(type(data))

#acessar as dimesoes(numero de linhas e de colunas) da tabela
print(data.shape)
print(f"O dataset possui {data.shape[0]} linhas e {data.shape[1]} colunas")