import streamlit as st
from random import randint

st.title('Gerador de Números Aleatórios')

if 'ultimo_numero' not in st.session_state:
    st.session_state.ultimo_numero = 'Nenhum número foi gerado'

st.subheader(f'Último número gerado: {st.session_state.ultimo_numero}')

if st.button('Gerar'):
    num_gerado = randint(1, 100)
    st.subheader(f'O número gerado foi: {num_gerado}')
    st.session_state.ultimo_numero = num_gerado