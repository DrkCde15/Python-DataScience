import pandas as pd

#carregando dataset usando o ';' como separador
data =pd.read_csv('./datasets/GasPricesinBrazil_2004-2019.csv', sep=';')
print(data.head(6))

print(data.PRODUTO) #imprimindo a coluna PRODUTO

print(data.PRODUTO.copy()) #criando uma copia da coluna PRODUTO

new_product = data['PRODUTO'] = 'Combustivel' #criando uma nova coluna e atribuindo um valor

print(new_product)   #atribuindo um valor constante 'Combustivel' para a coluna PRODUTO
print(data.head())

nrowls, ncols = data.shape #atribuindo o numero de linhas e colunas
print(f"O dataset possui {nrowls} linhas e {ncols} colunas") #numero de linhas de colunas

new_pd = [f'Produto {i}' for i in range(nrowls)] # criando uma lista com os nomes dos produtos de acordo com o numero de linhas
print(new_pd)

print(data.shape) #mostra o numero de linhas e colunas
print('\n')
print(data.PRODUTO.copy()) #mostra a coluna PRODUTO com os novos nomes