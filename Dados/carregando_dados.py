import pandas as pd

#carregando dataset usando o ';' como separador
df_frame = pd.read_csv('./datasets/GasPricesinBrazil_2004-2019_new.csv', sep=';', encoding='latin1', low_memory=False)
print(df_frame)

pd.set_option('display.max_columns', None) #mostra todas as colunas do dataframe

colun = df_frame["PRODUTO"].str.lower()
print(colun)