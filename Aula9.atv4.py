numero = float(input("DIGITE UM NÚMERO: "))
if numero % 2 ==0 :
    if numero > 0:
        print("SEU NÚMERO É POSITIVO")
    else:
        print("SEU NÚMERO É NEGATIVO")
    print("SEU NÚMERO É PAR")
elif numero % 1 ==0 :
    if numero > 0:
        print("SEU NÚMERO É POSITIVO")
    else:
        print("SEU NÚMERO É NEGATIVO")
    print("SEU NÚMERO É IMPAR")
else:
    print("ERRO")