import pandas as pd

#carregando dataset usando o ';' como separador
data =pd.read_csv('./datasets/GasPricesinBrazil_2004-2019.csv', sep=';')

#acessando colunas pelo nome
print(data['ESTADO'])
print(data.ESTADO)

print(data.iloc[4]) #acessando linhas pelo index

print(pd.Series(['a', 'b', 'c'])) #criando uma series a partir de uma lista de strings
print(pd.Series([1, 2, 3])) #criando uma series a partir de uma lista de inteiros
print(pd.Series([5.5, 6.0, 3.9])) #criando uma series a partir de uma lista de floats

print(pd.Series([5.5, 6.0, 3.9], index= ['P1', 'P2', 'P3'], name= 'Provas')) #criando uma series a partir de uma lista de floats com index e nome da series