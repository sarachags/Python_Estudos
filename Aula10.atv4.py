rec='sim'
while rec=='sim':
    inicio = int(input("DIGITE A HORA DE INICIO DA PARTIDA: "))
    fim = int(input("DIGITE A HORA DE FIM DA PARTIDA: "))

    if  inicio<fim:
        duracao = fim - inicio
        print(duracao,"horas")
    else:
        print(24-incio+fim)
        rec = input("DESEJA RECOMEÇAR? ")
        continue
else:
    print("FIM")