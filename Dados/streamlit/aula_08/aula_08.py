import streamlit as st

st.title("Calculadora")

st.header("Digite dois numeros")

num1 = st.number_input(label='Digite o primeiro numero', format='%.0f')
num2 = st.number_input(label='Digite o segundo numero', format='%.0f')

st.markdown('Escolha uma operação')

colums = st.columns(4)

with colums[0]:
    if st.button('Somar', use_container_width=True):
        st.write(f'A soma é {num1 + num2}')
        
with colums[1]:
    if st.button('Subtrair', use_container_width=True):
        st.write(f'A subtração é {num1 - num2}')

with colums[2]:
    if st.button('Multiplicar', use_container_width=True):
        st.write(f'A multiplicação é {num1 * num2}')

with colums[3]:
    if st.button('Dividir', use_container_width=True):
        st.write(f'A divisão é {num1 / num2}')