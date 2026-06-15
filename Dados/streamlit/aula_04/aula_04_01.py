import streamlit as st

st.title('Contador e Estado da Sessão')

if 'count' not in st.session_state:
    st.session_state.count = 0

def increment_count():
    st.session_state.count += 1

st.button('Incrementar Contador', on_click=increment_count)

st.write(f'Estado da Sessão: {st.session_state.count}')

st.header('Formulario de estado')

if 'user_name' not in st.session_state:
    st.session_state.user_name = ''

def update_name():
    st.session_state.user_name = st.session_state.user_name_input

st.text_input(
    label='Digite seu nome',
    key='user_name_input',
    on_change=update_name
)

st.write(f'Nome salvo, olá, {st.session_state.user_name}!')