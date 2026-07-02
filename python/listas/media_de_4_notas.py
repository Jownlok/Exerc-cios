notas = []

for i in range(4):
    nota = float(input('Digite a nota: '))
    notas.append(nota)

media = sum(notas) / len(notas)
print(f'As notas são: {notas}\n', f'A média das notas é: {media:.2f}')