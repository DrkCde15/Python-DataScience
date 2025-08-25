import pandas as pd

dtfm = pd.DataFrame(
    {
        'Categoria':['Calças', 'Vestidos', 'Camisas'],
        'Valor':[12, 42, 32]
    })
dtfm = pd.DataFrame(dtfm)
    
result = dtfm.groupby('Categoria')['Valor'].agg(['sum', 'mean', 'max'])
    
print(result)