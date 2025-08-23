import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('./produtos_ficticios.xlsx')
# print (df)

# Gráfico de Dispersão
sns.scatterplot(data=df, x='Preço', y='Categoria')

plt.show()