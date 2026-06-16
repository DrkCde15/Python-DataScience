import streamlit as st
from datetime import date, time

st.title('Widgets de Entrada')
st.header('Seleção de opções')

# Caixa de seleção
option = st.selectbox(
    label='Qual é o seu sexo?',
    options=['Feminino', 'Masculino']
)

st.write('Você selecionou:', option)

# Caixa de seleção multipla
options = st.multiselect(
    label='Quais suas cores favoritas?',
    options=['Vermelho', 'Verde', 'Azul', 'Amarelo'],
    placeholder='Selecione uma ou mais cores'
)

st.write(f'Você selecionou: {', '.join(options) if options else 'Nenhuma'}')

# Radio Button
color = st.radio(
    label='Qual é a sua cor favorita?',
    options=['Vermelho', 'Verde', 'Azul', 'Amarelo']
)

st.write(f'Você selecionou: {color}')

# Seleção de Data/Horas

data = st.date_input(
    label='Qual é a sua data de nascimento?',
    value=date(2000, 1, 1),
    min_value=date(1900, 1, 1),
    max_value=date.today()
)

st.write(f'Você nasceu em: {data}')

hora = st.time_input(label='Selecione um horário',
    value=time(12, 0)
)

st.write(f'Você selecionou: {hora}')

# Checkbox e Download
caixa_select = st.checkbox(label='Aceito os Termos')

if caixa_select:
    st.write('Você aceitou os termos')
    st.download_button(
        label='Baixar arquivo',
        data='Conteúdo do arquivo',
        file_name='arquivo.txt',
        mime='text/plain'
)
else:
    st.info('ACEITA OS TERMOS')
    
# Criação de formulário
with st.form(key='form1'):
    nome = st.text_input(label='Nome')
    email = st.text_input(label='Email')
    text = st.text_area(label='Mensagem')
    enviar = st.form_submit_button(label='Enviar')

if enviar:
    if nome and email and text:
        st.write(f'Nome: {nome}')
        st.write(f'Email: {email}')
        st.write(f'Mensagem: {text}')
    else:
        st.error('Preencha todos os campos do formulário')