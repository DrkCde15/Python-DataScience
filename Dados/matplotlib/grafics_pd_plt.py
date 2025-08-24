import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('./indexData.csv', sep=',')
# print(df)
# print(df.columns)
df_1 = df[['Index','Date', 'Close']]
# print(df_1)

df_rm = df_1.loc[(df_1['Index']!='NYA')]
df_final = df_1.drop(df_rm.index) 
# print(df_final)

df_final = df_final[13900:]
# print(df_final)

fig = plt.figure(figsize=(20,4))
fig.add_subplot(131)
plt.plot(df_final['Date'], df_final['Close'], label='NYA', color='m', ls ='--', lw=2.0)
plt.legend(loc=2)
plt.ylabel('Fechamento')
plt.xlabel('Data')
plt.title('Gráfico Linha')
plt.axis('auto')
plt.tight_layout()

fig.add_subplot(132)
plt.bar(df_final['Date'], df_final['Close'], label='NYA', color='b', lw=2.0)
plt.legend(loc=1)
plt.ylabel('Fechamento')
plt.xlabel('Data')
plt.title('Gráfico Barras')
plt.axis('auto')
plt.tight_layout()

fig.add_subplot(133)
plt.scatter(df_final['Date'], df_final['Close'], label='NYA', color='r', lw=2.0)
plt.legend(loc=1)
plt.ylabel('Fechamento')
plt.xlabel('Data')
plt.title('Gráfico Pontos')
plt.axis('auto')
plt.tight_layout()

plt.savefig('./figs/data_close.png')
plt.show()