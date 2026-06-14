import streamlit as st

st.title("Calculadora")

st.header("Digite dois numeros")

num = st.number_input(label='Digite o primeiro numero')
num2 = st.number_input(label='Digite o segundo numero')

st.markdown("Escolha a operação")

soma = st.button('+')
sub = st.button('-')
mult = st.button('x')
dvd = st.button('/')

if soma:
    st.write(f'O resultado da soma é {num + num2}')
elif sub:
    st.write(f'O resultado da subtração é {num - num2}')
elif mult:
    st.write(f'O resultado da multiplicação é {num * num2}')
elif dvd:
    st.write(f'O resultado da divisão é {num / num2}')