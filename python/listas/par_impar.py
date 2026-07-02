lista_par = []
lista_impar = []

for i in range(20):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
print(f'Lista de números pares: {lista_par}\n', f'Lista de números ímpares: {lista_impar}')