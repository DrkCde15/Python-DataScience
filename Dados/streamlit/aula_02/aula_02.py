import streamlit as st

st.title("Iteração Layout")

# Barra lateral
st.sidebar.header("Opções da aplicação")

# Botões
nome = st.sidebar.text_input(label='Digite o nome')
st.sidebar.write(f'Olá {nome}')

# Colunas para organizar o conteúdo
colums = st.columns(2)

with colums[0]:
    st.header('Interações simples')
    if st.button('Clique'):
        st.success('Você clicou no botão')
    slider = st.slider(
        label='Escolha um valor',
        min_value=0,
        max_value=10,
        value=5
    )
    st.write(f'O valor escolhido foi {slider}')
    
with colums[1]:
    st.header('Infos e imagens')
    st.info('Esta é uma mensagem informativa')
    
    # Imagem
    st.image(image=r'C:\Users\Júlio César\Pictures\download (2).jpeg', 
             width='stretch', 
             caption='Carro Vermelho'
    )
    
    st.warning('Atenção seu comédia')
    
# Entrada de numero
num = st.number_input(label='Digite um numero')
st.write(f'O numero digitado foi {num}')