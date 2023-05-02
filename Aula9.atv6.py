recomecar = 'sim'
while recomecar == 'sim':
    altura = int(input("DIGITE A ALTURA DO TRIÂNGULO: "))
    base = int(input("AGORA DIGITE A BASE: "))
    a=(altura*base)/2
    print("A ÁREA DO SEU TRIÂNGULO É", a)
    recomecar = input("DIGITE 'SIM' PARA RECOMECAR: ")
else:
    print("FIM")
