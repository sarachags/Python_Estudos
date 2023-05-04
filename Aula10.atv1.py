recomecar = 'sim'
while recomecar == 'sim':
    escolha = int(input("1- TRIÂNGULO \n2 - RETÂNGULO \n3 - FINALIZAR \nDIGITE SUA ESCOLHA: "))

    if escolha ==1:
        altura_t = float(input("DIGITE A ALTURA DO SEU TRIANGULO: "))
        base_t = float(input("DIGITE A BASE DO SEU TRIANGULO: "))
        triangulo = (altura_t * base_t)/2
        print("SUA ÁREA É", triangulo)

    elif escolha==2:
        altura_r = float(input("DIGITE A ALTURA DO SEU RETÂNGULO: "))
        base_r = float(input("DIGITE A BASE DO SEU RETÂNGULO: "))
        retangulo = (altura_r * base_r)
        print("SUA ÁREA É", retangulo)

    elif escolha == 3:
        print("ATÉ LOGO")
        break

    else:
        print("Escolha errada, escolha novamente")
        continue
    recomecar = (input("DESEJA CALCULAR NOVAMENTE? "))


else:
    print("fim")