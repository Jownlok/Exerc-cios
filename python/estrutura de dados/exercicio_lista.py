notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

print(notas.count(7)) #Count é uma função de lista que conta a quantidade de número x
notas[-1] = 4 #Remove o último item e substitui por 4
print(max(notas)) #Acha o maior número dentro da lista
notas.sort() #Ordena as notas
print(notas)
print(sum(notas) / len(notas)) #Sum soma todos números e len usado para medir a quantidade = média

