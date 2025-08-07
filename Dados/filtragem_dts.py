import pandas as pd

#carregando dataset usando
data = pd.read_csv('./datasets/GasPricesinBrazil_2004-2019.csv', sep=';')
print(data.head(6))

#filtrando amostras
print(data['ESTADO'].unique()) #imprimindo os estados unicos
print([data['ESTADO'] == 'SAO PAULO']) #faz uma comparação com o estado SAO PAULO retornando um booleano

selecao = data['ESTADO'] == 'SAO PAULO'
print(selecao) #imprimindo o booleano da comparação com o estado SAO PAULO

print(type(selecao)) #imprimindo o tipo do booleano
print(selecao.shape) #imprimindo o shape do booleano
print(data.shape) #imprimindo o shape do dataframe

print(data[selecao]) #imprimindo as linhas onde o estado eh SAO PAULO

print(data.loc[selecao]) #imprimindo as linhas onde o estado eh SAO PAULO

print(data.query('ESTADO == "SAO PAULO"')) #imprimindo as linhas onde o estado eh SAO PAULO

postos_sp = data.query('ESTADO == "SAO PAULO"')
print(postos_sp.reset_index()) #imprimindo as linhas onde o estado eh SAO PAULO e resetando o index das linhas para 0

print(postos_sp.reset_index(drop=True)) #imprimindo as linhas onde o estado eh SAO PAULO e resetando o index das linhas para 0

postos_sp.reset_index(drop=True, inplace=True) #resetando o index das linhas para 0 e salvando no dataframe
print(postos_sp)