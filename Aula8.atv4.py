recomecar = "sim"
while recomecar == "sim":
    nota1 = float(input("DIGITE A NOTA 1: "))
    nota2 = float(input("DIGITE A NOTA 2: "))
    media= (nota1 + nota2)/2
    if media>=7:
        print("ALUNO APROVADO")
    elif media>=4:
        print("ALUNO EM RECUPERAÇÃO")
    else:
        print("ALUNO REPROVADO")
    print ("SUA MEDIA É: ", media)
    recomecar = input("DESEJA RECOMEÇAR? ")
else:
    print ("OBRIGADO E ATÉ LOGO!")