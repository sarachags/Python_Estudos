quantidade = int(input("ESCREVA QUANTAS MAÇÃS VOCÊ DESEJA: "))
if quantidade<12:
    print("R$"f"{quantidade * 1.3:.2f}")
else:
    print("R$",quantidade * 1.0)
