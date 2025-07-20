nome  = input("Digite seu nome: ")
alt = float(input("Digite sua altura: "))

if alt < 1.0:
    print(f"seu nome eh {nome} e voce esta na categoria de altura Anãzinha")
elif alt < 1.6:
    print(f"seu nome eh {nome} e voce esta na categoria de altura Baixinha")
elif 1.6 <= alt <= 1.8:
    print(f"seu nome eh {nome} e voce esta na categoria de altura Normal")
elif 1.8 < alt <= 2.1:
    print(f"seu nome eh {nome} e voce esta na categoria de altura Amazona")
elif  2.1 < alt <= 3.0:
    print(f"seu nome eh {nome} e voce esta na categoria de altura Morte por snu snu")
else:
    print(f"seu nome eh {nome} e voce esta na categoria de altura do Godzilla")
