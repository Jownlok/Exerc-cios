total = []

for i in range(4):
    nome = input('Digite o nome do aluno: ')
    
    nota = int(input('Digite a nota 1: '))
    nota2 = int(input('Digite a nota 2: '))
    nota3 = int(input('Digite a nota 3: '))
    nota4 = int(input('Digite a nota 4: '))
    
    media = (nota + nota2 + nota3 + nota4) / 4
    
    total.append([nome, media])

print("\nAlunos com média maior que 7:\n")

for aluno in total:
    if aluno[1] > 7:
        print(aluno[0], aluno[1])