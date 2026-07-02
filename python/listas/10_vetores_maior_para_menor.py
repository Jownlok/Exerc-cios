lista = []
for i in range(10):
    numero = int(input('Digite um número inteiro: '))
    lista.append(numero)
lista.sort(reverse=True) #Usado para organizar itens do maior para menor
print('Lista em ordem decrescente:', lista)