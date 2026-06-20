
print('1 - Adição')
print('2 - Subtração')
print('3 - Sair')

total = 0

while True:
    op = int(input('Digite a opção desejada:'))
    if op == 1:
        num = int(input('Digite um número:'))
        total = total + num
        print('Total:', total)
    elif op == 2:
        num = int(input('Digite um número:'))
        total = total - num
        print('Total:', total)
    elif op == 3:
        print('Encerrando...')
        break
    else:
        print('Opção inválida!')