senha="2222"
login = input("DIGITE SUA SENHA: ")
contador=1
while login!=senha:
    login = input("SENHA INCORRETA DIGITE NOVAMENTE: ")
    contador=contador+1
    if login!=senha and contador==3:
        print("ERRO! TENTATIVAS BLOQUEADAS!")
else:
    print("SENHA CORRETA. SEJA BEM VINDO(A)")