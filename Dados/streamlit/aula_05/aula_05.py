import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

st.title('Visualização de Dados')

# Criação do DataFrame
df = pd.DataFrame(
    {
        'data': pd.to_datetime(pd.date_range(start='2026-01', periods=100)),
        'valor_a': np.random.rand(100).cumsum(),
        'valor_b': np.random.rand(100).cumsum() + 10
    }
)

# Gráfico com o Matplotlib
st.header('Matplotlib')
fig, ax = plt.subplots()

ax.plot(df['data'], df['valor_a'], label='Valor A', color='red')
ax.plot(df['data'], df['valor_b'], label='Valor B', color='blue')

ax.set_xlabel('Data')
ax.set_ylabel('Valores')
ax.set_title('Gráfico de Linhas')
ax.xaxis.set_major_locator(mdates.DayLocator(interval=10))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
plt.xticks(rotation=45)
ax.legend()
ax.grid(True)
fig.tight_layout()
st.pyplot(fig)

# Gráfico com o Plotly
st.header('Plotly')
fig_plotly = px.line(df, x='data', y=['valor_a', 'valor_b'], title='Gráfico de Linhas')
st.plotly_chart(fig_plotly)

# Gráfico com Altair
st.header('Altair Ibn La Ahad')
chart = alt.Chart(df).mark_line().encode(
    x='data',
    y=alt.Y('valor_a', title='Valor A'),
    color=alt.value('white'),
    tooltip=['data', 'valor_a', 'valor_b']
).properties(
    width=800,
    height=400
)
st.altair_chart(chart, use_container_width=True)