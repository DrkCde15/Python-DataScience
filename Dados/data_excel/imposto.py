import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os

def calcular_ir(rendimento_anual, dependentes=0, gastos_saude=0, gastos_educacao=0, inss=0, pgb_l=0):
    deducao_dependente = 189.59 * 12
    deducao_educacao = min(gastos_educacao, 3561.50)
    deducao_pgb_l = min(pgb_l, rendimento_anual * 0.12)

    total_deducoes = (
        inss + gastos_saude + deducao_educacao +
        (dependentes * deducao_dependente) + deducao_pgb_l
    )

    base_calculo = rendimento_anual - total_deducoes
    base_mensal = base_calculo / 12

    # Tabela IRPF 2025
    if base_mensal <= 2259.20:
        aliquota = 0.0
        deducao = 0.0
    elif base_mensal <= 2826.65:
        aliquota = 0.075
        deducao = 169.44
    elif base_mensal <= 3751.05:
        aliquota = 0.15
        deducao = 381.44
    elif base_mensal <= 4664.68:
        aliquota = 0.225
        deducao = 662.77
    else:
        aliquota = 0.275
        deducao = 896.00

    ir_mensal = max(0, (base_mensal * aliquota) - deducao)
    ir_anual = ir_mensal * 12

    return {
        "Base de cálculo (R$)": round(base_calculo, 2),
        "Alíquota (%)": f"{aliquota * 100:.1f}",
        "IR Mensal (R$)": round(ir_mensal, 2),
        "IR Anual (R$)": round(ir_anual, 2)
    }

def gerar_relatorio():
    try:
        rendimento_mensal = float(entry_rendimento.get())
        dependentes = int(entry_dependentes.get())
        gastos_saude = float(entry_saude.get())
        gastos_educacao = float(entry_educacao.get())
        inss = float(entry_inss.get())
        pgb_l = float(entry_pgbl.get())

        rendimento_anual = rendimento_mensal * 12

        resultado = calcular_ir(
            rendimento_anual, dependentes, gastos_saude,
            gastos_educacao, inss, pgb_l
        )

        dados = {
            "Rendimento Mensal (R$)": [rendimento_mensal],
            "Rendimento Anual (R$)": [rendimento_anual],
            "Dependentes": [dependentes],
            "Saúde (R$)": [gastos_saude],
            "Educação (R$)": [gastos_educacao],
            "INSS (R$)": [inss],
            "PGBL (R$)": [pgb_l],
            **resultado
        }

        df_novo = pd.DataFrame(dados)

        if os.path.exists("relatorio_irpf.xlsx"):
            df_existente = pd.read_excel("relatorio_irpf.xlsx")
            df_atualizado = pd.concat([df_existente, df_novo], ignore_index=True)
        else:
            df_atualizado = df_novo

        df_atualizado.to_excel("relatorio_irpf.xlsx", index=False)

        detalhes = "\n".join([f"{k}: {v}" for k, v in resultado.items()])
        messagebox.showinfo("Resultado do IRPF", detalhes)
        messagebox.showinfo("Excel", "Relatório atualizado com sucesso!")

    except ValueError:
        messagebox.showerror("Erro", "Preencha todos os campos corretamente.")

# =============== GUI ===============
janela = tk.Tk()
janela.title("Calculadora de IRPF 2025")
janela.geometry("400x520")
janela.resizable(False, False)

largura_entry = 30

campos = [
    ("Rendimento Mensal (R$):", "rendimento"),
    ("Nº de Dependentes:", "dependentes"),
    ("Gastos com Saúde (R$):", "saude"),
    ("Gastos com Educação (R$):", "educacao"),
    ("INSS Pago (R$):", "inss"),
    ("PGBL Pago (R$):", "pgbl"),
]

entry_dict = {}

for label_text, key in campos:
    tk.Label(janela, text=label_text).pack(pady=5)
    entry = tk.Entry(janela, width=largura_entry)
    entry.pack()
    entry_dict[key] = entry

entry_rendimento = entry_dict["rendimento"]
entry_dependentes = entry_dict["dependentes"]
entry_saude = entry_dict["saude"]
entry_educacao = entry_dict["educacao"]
entry_inss = entry_dict["inss"]
entry_pgbl = entry_dict["pgbl"]

tk.Button(janela, text="Calcular IR", command=gerar_relatorio, bg="green", fg="white").pack(pady=20)

janela.mainloop()
