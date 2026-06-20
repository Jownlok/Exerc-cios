a = 80000
b = 200000
anos = 0

while a != b:
    a = a / 3 * 100 + a
    b = b / 1.5 * 100 + b
    anos = anos + 1

print(f'É preciso de {anos} anos para cidade a atingir a população de b')