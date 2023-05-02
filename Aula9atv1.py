reescrever = "ok"
while reescrever == "ok":
    numero = float(input("DIGITE UM NÙMERO: "))
    if numero != 0:
        if numero > 0:
            print("SEU NÚMERO É POSITIVO")
        else:
            print("SEU NÚMERO É NEGATIVO")
    else:
        print("ESCREVA 'OK' E REESCREVA UM NÚMERO DIFERENTE DE 0")
        continue
    reescrever=input("DESEJA RECOMEÇAR? ")
else:
    print("FIM")