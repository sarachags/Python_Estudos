nota1 = int(input("DIGITE SUA PRIMEIRA NOTA: "))
contador=0
while -1<=nota1>=11:
    nota1 = int(input("DIGITE SUA PRIMEIRA NOTA DE 0 A 10: "))
nota2 = int(input("DIGITE SUA SEGUNDA: "))
while -1<=nota2>=11:
    nota2 = int(input("DIGITE SUA SEGUNDA NOTA DE 0 A 10: "))
media=(nota1+nota2)/2
print("SUA MÉDIA É: ", media)