G = 5.80
E = 4.90
C = input("G - Gasolina \nE - Etanol \nInsira Aqui Qual o Seu Combustivel: ")
Litros = float(input("Quantos Litros De Combustivel Deseja? "))
if C in "Gg":
    total = G * Litros
    print(total)
elif C in "Ee":
    total = E * Litros
    print(total)
else:
    print("ERRO! TIPO INVALIDO")
