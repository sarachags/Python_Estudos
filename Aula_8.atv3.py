vetor=[]
for x in range(4):
    vetor.append(int(input("DIGITE UM VALOR: ")))

for y in range(10):
   if vetor[y] % 2 == 0:
       print(vetor[y])

contador=0
media = int(input("DIGITE UMA MÉDIA: "))
for w in range(10):
   if vetor[w] >= media:
       contador=contador+1
print(contador)

maior=vetor[0]
menor=vetor[0]

for z in range(4):
    if vetor[z] > maior:
        maior = vetor[z]
    elif vetor[z] < menor:
        menor = vetor[z]
print ("O maior é", maior, "e o menor é", menor)
