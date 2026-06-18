import numpy as np
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

st.set_page_config(layout='wide')

st.title('Métricas')

np.random.seed(42)

data = pd.DataFrame({
    'mes': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
            'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    'vendas_atual': np.random.randint(8000, 15000, 12),
    'vendas_anterior': np.random.randint(7000, 14000, 12)
})

st.subheader('Tabela de Dados')
st.dataframe(data)

total_vendas_atual = data['vendas_atual'].sum()
total_vendas_anterior = data['vendas_anterior'].sum()
delta_vendas = total_vendas_atual - total_vendas_anterior
percentual_delta = (delta_vendas / total_vendas_anterior) * 100
media_mensal = data['vendas_atual'].mean()
media_mensal_anterior = data['vendas_anterior'].mean()
delta_media_mensal = media_mensal - media_mensal_anterior
percentual_delta_media_mensal = (delta_media_mensal / media_mensal_anterior) * 100

st.divider()
st.subheader('Métricas estáticas')

colums = st.columns(3)
with colums[0]:
    st.metric(
        label='Total de vendas atual', 
        value=f'R$ {total_vendas_atual:.2f}',
        delta = f'R$ {delta_vendas:.2f}'
    )
    
with colums[1]:
    st.metric(
        label='Total de vendas anterior', 
        value=f'R$ {total_vendas_anterior:.2f}',
        delta = f'R$ {delta_vendas:.2f}'
    )
    
with colums[2]:
    st.metric(
        label='Média mensal de vendas', 
        value=f'R$ {media_mensal:.2f}',
        delta = f'R$ {percentual_delta_media_mensal:.2f}'
    )
    
st.divider()
st.subheader('Métricas dinamicas')

mes_selecionado = st.selectbox(label='Selecione um mês', options=data['mes'])

row_filter = data[data['mes'] == mes_selecionado].iloc[0]

vendas_atual_mes = row_filter['vendas_atual']
vendas_anterior_mes = row_filter['vendas_anterior']
delta_vendas_mes = vendas_atual_mes - vendas_anterior_mes
delta_formatado = ''
if delta_vendas_mes > 0:
    delta_formatado = f'+ R$ {delta_vendas_mes:.2f}'
elif delta_vendas_mes < 0:
    delta_formatado = f'- R$ {abs(delta_vendas_mes):.2f}'
else:
    delta_formatado = 'R$ 0.00'

st.metric(
    label= f'Vendas de {mes_selecionado}',
    value=f'R$ {vendas_atual_mes:.2f}',
    delta=delta_formatado
)

st.divider()
st.subheader('Gráficos dinâmicos')

generator = rng(4)

mudancas = list(generator.standard_normal(12))

dados = [sum(mudancas[:i+1]) for i in range(20)]

delta = round(dados[-1], 2)

colunas = st.columns(3)

with colunas[0]:
    st.metric(
        label='Indicador (linha)',
        value=10,
        delta=delta,
        chart_data=dados,
        chart_type='line',
        border=True
    )

with colunas[1]:
    st.metric(
        label='Indicador (área)',
        value=10,
        delta=delta,
        chart_data=dados,
        chart_type='area',
        border=True
    )

with colunas[2]:
    st.metric(
        label='Indicador (barra)',
        value=10,
        delta=delta,
        chart_data=dados,
        chart_type='bar',
        border=True
    )