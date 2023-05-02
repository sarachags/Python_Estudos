# n1 = float(input("DIGITE UM NÚMERO: "))
# n2 = float(input("DIGITE UM NÚMERO: "))
# n3 = float(input("DIGITE UM NÚMERO: "))
# n4 = float(input("DIGITE UM NÚMERO: "))
# media = (n1+n2+n3+n3)/4
# media1 = n1+n2+n3+n4
# print("A MÉDIA É", media, "E A SOMA É", media1)

vetor=[]
soma = 0
for x in range(4):
    vetor.append(float(input("DIGITE O NÚMERO: ")))
    soma = soma + vetor[x]
    media = soma/4
print("SUA SOMA É", soma, "SUA MÉDIA É", media)
