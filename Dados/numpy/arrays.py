import numpy as np

# Arrays criados a partir de listas
qtde = [2, 5, 10, 20, 35]
custo = [100, 150, 450, 320, 195]

arr_1 = np.array(qtde)
arr_2 = np.array(custo)

# Operações vetoriais (multiplicação elemento a elemento)
estq = arr_1 * arr_2
print(f"Estoque: {estq}")

cst = [100, 200, 300, 400]
vnd = [125, 255, 355, 409]

arr_3 = np.array(cst)
arr_4 = np.array(vnd)

# Subtração elemento a elemento
lcr = arr_4 - arr_3
print(f"Lucro: {lcr}")


# Criação de arrays com funções do NumPy
print(np.arange(10, 21))              # de 10 até 20
print(np.arange(10, 21, 2))           # de 10 até 20, pulando de 2 em 2
print(np.arange(10, 21, 2, dtype=float))

print(np.linspace(0, 2, 10))          # 10 valores igualmente espaçados entre 0 e 2


# Geração de números aleatórios
print('\n', np.random.rand(10))        # 10 valores ~ U(0,1)
print('\n', np.random.randn(10))       # 10 valores ~ distribuição normal
print('\n', np.random.randint(10, 100, 30)) # 30 inteiros aleatórios entre 10 e 99


# Matrizes especiais
print(np.zeros((5, 4)))  # matriz 5x4 só de zeros
print(np.ones((5, 5)))   # matriz 5x5 só de uns
print(np.eye(6))         # matriz identidade 6x6


# Arrays unidimensionais
arr = np.arange(1, 11, dtype=int)
print(arr)
print(arr[4])      # índice único
print(arr[2:5])    # slice do índice 2 até 4
print(arr[:5])     # do início até o índice 4
print(arr[2:])     # do índice 2 até o final


# Arrays bidimensionais
arr_2 = np.random.randint(10, 50, size=(3, 3))
print(arr_2)

# Acesso [linha][coluna]
print(arr_2[1][1])   # linha 1, coluna 1
print(arr_2[1][2])   # linha 1, coluna 2
print(arr_2[2])      # linha 2 inteira
print(arr_2[2][1])   # linha 2, coluna 1
