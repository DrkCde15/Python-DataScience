"""
Pandas: Agregação de dados com GroupBy.

Demonstra como agrupar dados por categoria e aplicar
múltiplas funções de agregação (soma, média, máximo).
"""
import pandas as pd

# DataFrame simples com categorias e valores
dtfm = pd.DataFrame(
    {
        'Categoria': ['Calças', 'Vestidos', 'Camisas'],
        'Valor': [12, 42, 32]
    })

# Agrupa por 'Categoria' e aplica agregações na coluna 'Valor'
result = dtfm.groupby('Categoria')['Valor'].agg(['sum', 'mean', 'max'])

print(result)