recomecar = 'sim'
def soma(n1,n2):
    print(n1+n2)
def subtrair(n1,n2):
    print(n1-n2)
def multiplicar(n1,n2):
    print(n1*n2)
def dividir(n1,n2):
    print(n1/n2)

while recomecar == 'sim':
    escolha = int(input("SOMAR: 1 \nSUBTRAIR: 2 \nMULTIPLICAR: 3 \nDIVIDIR: 4 \nSAIR: 5 \nDIGITE SUA ESCOLHA: "))
    if escolha == 1:
        n1 = int(input("ESCOLHA UM NÚMERO: "))
        n2 = int(input("ESCOLHA UM NÚMERO: "))
        soma(n1,n2)

    elif escolha == 2:
        n1 = int(input("ESCOLHA UM NÚMERO: "))
        n2 = int(input("ESCOLHA UM NÚMERO: "))
        subtrair(n1,n2)

    elif escolha == 3:
        n1 = int(input("ESCOLHA UM NÚMERO: "))
        n2 = int(input("ESCOLHA UM NÚMERO: "))
        multiplicar(n1, n2)

    elif escolha == 4:
        n1 = int(input("ESCOLHA UM NÚMERO: "))
        n2 = int(input("ESCOLHA UM NÚMERO: "))
        dividir(n1,n2)

    if escolha == 5:
        print("OBRIGADO E ATÉ LOGO!")
        break
    recomecar=input("DESEJA RECOMEÇAR? ")
    continue

else:
    print("OBRIGADO E ATÉ LOGO!")