def soma(n1,n2):
    print(n1+n2)
def subtrair(n1,n2):
    print(n1-n2)
def multiplicar(n1,n2):
    print(n1*n2)
def dividir(n1,n2):
    print(n1/n2)

# --------------------------------------------------------

def imprime_nome(nome):
    print(f"NOME: {nome[::-1]}")

# --------------------------------------------------------

# def repeticao(n):
#     for x in range(1,n+1):
#         for y in range(1,x+1):
#             print(y, end=" ")
#         print()


# ---------------------------------------------------------

def valor_estoque(nome, quantidade, valor_unitario):
    valor_do_estoque = quantidade * valor_unitario
    return nome, valor_do_estoque

# ---------------------------------------------------------

def contar_vogais(texto):
    i=0
    for x in texto:
        if x in "AaEeIiOoUu":
            i += 1
    print(i)

# ---------------------------------------------------------

def argumento(numero):
    if numero > 0:
        return 'P'
    elif numero < 0:
        return 'N'
    else:
        return 'Z'

# ----------------------------------------------------------

def armazenar(a, b):
    produtos.append(a)
    precos.append(b)

produtos = []
precos = []
