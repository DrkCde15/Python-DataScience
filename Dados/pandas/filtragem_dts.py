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


print(data['PREÇO MÉDIO REVENDA'].unique()) #imprimindo os estados unicos
print(data['PREÇO MÉDIO REVENDA']) #imprimindo a coluna PREÇO MÉDIO REVENDA

selecao = (data['ESTADO'] == 'RIO DE JANEIRO') & (data['PREÇO MÉDIO REVENDA']> 2.0) #imprimindo as linhas onde o estado eh RIO DE JANEIRO e a coluna PREÇO MÉDIO REVENDA eh maior que 2
print(selecao)

selecao = (data['ESTADO'] == 'RIO DE JANEIRO') | (data['PREÇO MÉDIO REVENDA']> 2.0) #imprimindo as linhas onde o estado eh RIO DE JANEIRO ou a coluna PREÇO MÉDIO REVENDA eh maior que 2
print(selecao)

selecao = (data['ESTADO'] == 'RIO DE JANEIRO') != (data['PREÇO MÉDIO REVENDA']> 2.0) #imprimindo as linhas onde o estado eh RIO DE JANEIRO e a coluna PREÇO MÉDIO REVENDA eh maior que 2
print(selecao)

print(data[selecao])

select_1 = (data['ESTADO'] == 'RIO DE JANEIRO')
df_rj = data[select_1]
print(df_rj)

select_2 = df_rj['PREÇO MÉDIO REVENDA'] > 2.0
print(select_2)

df_rj_preco = df_rj[select_2]
print(df_rj_preco)

selecao = (data['ESTADO'] == 'RIO DE JANEIRO') | (data['ESTADO'] == 'SAO PAULO')
print(selecao)
print(data[selecao])

selecao_2 = (data['PRODUTO'] == 'GASOLINA COMUM')
print(selecao_2)
print(data[selecao_2])


select_3 = (data['PREÇO MÉDIO REVENDA']> 2.0)
print(select_3)
print(data[select_3])


select_final = selecao & selecao_2 & select_3
print(select_final)
print(data[select_final])


select = (data['ESTADO'] == 'RIO DE JANEIRO') | (data['ESTADO'] == 'SAO PAULO') & (data['PRODUTO'] == 'GASOLINA COMUM') & (data['PREÇO MÉDIO REVENDA']> 2.0)
print(select)
print(data[select])