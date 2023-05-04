array=[]
contador=0
impares=0
while True:
    if contador %2 != 0:
        array.append(contador)
        impares += 1

    contador=contador+1
    if impares == 10:
        break

print(array)