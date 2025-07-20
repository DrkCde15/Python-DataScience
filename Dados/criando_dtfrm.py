import pandas as pd

#Criando dataframe
personas_df = pd.DataFrame(
    {
        'nome': ['Batman', 'Coringa', 'Spiderman', 'Magneto', 'Goku', 'Freeza'],
        'idade': [32, 200, 26, 58, 45, 100],
        'poder': ['Dinnheiro', 'Loucura', 'Sentido Aranha', 'Controlar metal', 'KI', 'KI'],
        'eh_heroi': [True, False, True, False, True, False]
    })
print(personas_df)
print(personas_df.info())

#acessando colunas
print(personas_df.columns)

#acessando tipos de colunas
print(type(personas_df.columns))

#acessando colunas como uma lista
print(list(personas_df.columns))

#renomeando colunas
personas_df.rename(columns={
    'nome': 'Nomes dos personagens',
    'idade': 'Idade dos personagens',
    'poder': 'Poderes dos personagens',
    'eh_heroi': 'Eh Heroi'
}, inplace=True)
print(personas_df)