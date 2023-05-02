vetor=[]
for x in range(3):
    vetor.append(int(input("ESCREVA UM NÚMERO: ")))
maior=vetor[0]
for z in range(3):
    if vetor[z] > maior:
        maior = vetor[z]
print("O MAIOR NÚMERO É", maior)