def lista_unica(l):
    nova_lista=[]
    for x in l:
        if x not in nova_lista:
            nova_lista.append(x)
    print(nova_lista)

# def lista2(l):
#     print(list(set(l)))

a=[1,2,4,5,5,6,7,8,8]
lista_unica(a)