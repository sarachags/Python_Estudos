criar = input("CRIE UMA SENHA: ")
senha = input("DIGITE SUA SENHA: ")
contador=0
while criar!=senha:
    senha = input("SENHA INCORRETA DIGITE NOVAMENTE: ")
    contador=contador+1
    if contador==2:
        print("ERRO! TENTATIVAS BLOQUEADAS!")

print("SENHA CORRETA. SEJA BEM VINDO(A)")