P1 = input("Digite o seu nome completo: ")
print("Olá", P1, "vamos começar a preencher os seus dados")
P2 = int(input("Digite sua idade: "))
P3 = float(input("Digite seu salário: "))
P4 = float(input("Digite a porcentagem que deseja acrescentar ao seu salário: "))
Porcentagem = (P4/100) * P3
print("Seus Dados São: \n" "Nome:", P1, "\n Idade: ", P2, "\n Salário Anterior: ", P3, "\n Aumento:", Porcentagem,"\n Salário Atual: ", Porcentagem + P3)