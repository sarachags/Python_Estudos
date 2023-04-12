notas = 1
alunos = int(input("DIGITE A QUANTOS ALUNOS HÁ NA TURMA: "))
somador=0
while notas<=alunos:
    notas = notas+1
    valor = int(input("Digite as notas de cada aluno: "))
    somador=somador+valor
media=somador/alunos
print("A MÉDIA DA TURMA É:", media)