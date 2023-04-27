vetor = []
contador=0
for x in range(3):
    vetor.append(int(input("DIGITE UM VALOR: ")))

numero = int(input("ESCOLHA UM NÚMERO A SER COMPARADO: "))

for y in range(3):
    if numero==vetor[y]:
        contador=contador+1
print(contador)