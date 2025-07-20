nome = input("Digite seu nome: ")
peso = float(input("Digite o peso: "))

if 10 <= peso < 40:
    print(f"seu nome eh {nome} e voce esta na categoria de peso Raquitica")
    
elif peso <= 49:
    print(f"seu nome eh {nome} e voce esta na categoria de Peso normal")
    
elif 50 <= peso <= 60:
    print(f"seu nome eh {nome} e voce esta na categoria de Peso Ippo")
    
elif 60 <= peso <= 100:
    print(f"seu nome eh {nome} e voce esta na categoria de peso Delicia")
    
elif 100 < peso <= 200:
    print(f"seu nome eh {nome} e voce esta na categoria de peso Gostosa")
    
else:
    print(f"seu nome eh {nome} e voce esta na categoria de peso Thais Carla")
