#x = 3
#while(x <= 12):
#    print(x)
#    x += 1 

print('1 - Coxinha R$ 5,00')
print('2 - Suco R$ 3,00')
print('3 - Pastel R$ 10,00')
print('4 - Sair')

total = 0
while True:
    op = int(input('Digite qual opção de escolha: '))
    if op == 1:
        total = total + 5
    elif op == 2:
        total = total + 3
    elif op == 3:
        total = total + 10
    elif op == 4:
        break
print(f'Total: R$ {total:.2f}')