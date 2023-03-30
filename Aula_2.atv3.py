Nome = input("Digite o seu nome: ")
print("Seja Bem-Vindo(a)", Nome)
Nota1 = float(input("Digite sua nota 1: "))
Nota2 = float(input("Digite sua nota 2: "))
Nota3 = float(input("Digite sua nota 3: "))
M = (Nota1 + Nota2 + Nota3)/3
if M>=7:
    print("Parabéns! Você Foi Aprovado")

elif M>=4:
    print("Ok! Você Vai Para Recuperação")

else:
    print("Sinto Muito...Você Foi Reprovado")
