def armazenar(a, b):
    produtos.append(a)
    precos.append(b)

produtos = []
precos = []

while True:
    n1=input("PRODUTO: ")
    n2=float(input("PREÇO: "))
    armazenar(n1,n2)
    recomecar = input("RECOMECAR: ")
    if recomecar != 'sim':
        break
print(produtos)
print(precos)
