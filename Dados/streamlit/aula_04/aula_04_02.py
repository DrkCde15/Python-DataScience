import streamlit as st
import time

st.title('Otimizando o caching')

@st.cache_data(ttl=3600)
def simulator_operation(parametro):
    st.write(f'Executando operação demorada: {parametro}')
    time.sleep(3)
    return f'Resultado da operação: {parametro}: {time.time()}'

parametro = st.slider(
    label='Escolha um parametro',
    min_value=1,
    max_value=10,
    value=5
)

result = simulator_operation(parametro)
st.write(result)

st.button(label='limpar cache', on_click=st.cache_data.clear)