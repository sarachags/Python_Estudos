# for x in range(1,6):
#     print(x*[x])

# def exercicio(n):
#     for x in range(1, n +1):
#         print(str(x)*x)
# exercicio(5)

# num = int(input("digite "))
# def exercicio():
#     for x in range(1, num +1):
#         print(x*str(x))
# exercicio()

def repeticao(n):
    for x in range(1,n+1):
        for y in range(1,x+1):
            print(y, end=" ")
        print()
repeticao(10)