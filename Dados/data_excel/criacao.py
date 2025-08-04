import random
from openpyxl import *

workbook = Workbook() #criando um workbook
sheet = workbook.active #criando uma planilha ativa no workbook

sheet.title = "Estoque" #definindo o nome da planilha

headers = ["Produto", "Quantidade", "Preço"] #criando um cabecalho para a planilha

for colum, header in enumerate(headers, start=1): #criando uma coluna para cada cabecalho e atribuindo um valor
    sheet.cell(row=1, column=colum, value=header)



def gera_produto(): #criando uma funcao para gerar um produto aleatorio
    prefixos = ['Super', 'Mega', 'Gigante', 'Ultra', 'Power', 'Max']
    tipos = ['Wiget', 'Gadget', 'Device', 'Tool', 'Component']
    sufixos = ['Plus', 'Pro', 'X', '2000', 'Elite', 'Prime']
    return f'{random.choice(prefixos)} {random.choice(tipos)} {random.choice(sufixos)}' #gerando um produto aleatorio com prefixo, tipo e sufixo

num_produtos = 50

for row_num in range(2, num_produtos + 2): #criando uma linha para cada produto gerado
    produto = gera_produto()
    quantidade = random.randint(1, 1000)
    preco = round(random.uniform(10.0, 500.0), 2)
    sheet.cell(row=row_num, column=1, value=produto)
    sheet.cell(row=row_num, column=2, value=preco)
    sheet.cell(row=row_num, column=3, value=quantidade)


file_path = 'estoque.xlsx'
workbook.save(file_path) #salvando o workbook