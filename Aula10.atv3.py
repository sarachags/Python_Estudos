rec='sim'
while rec=='sim':
    v1 = float(input("ESCREVA UM VALOR: "))
    v2 = float(input("ESCREVA UM VALOR: "))
    if v1!=v2:
        if v1<v2:
            print(v1 ,",", v2)
        else:
            print(v2 ,",", v1)
    else:
        print("NÚMEROS IGUAIS, DIGITE NOVAMENTE")
    rec = input("DESEJA RECOMEÇAR? ")
    continue
else:
    print("FIM")