print('-' * 30)
print('Calculadora')
print('Soma (+)')
print('Subtração (-)')
print('Multiplicação (*)')
print('Divisão (/)')
print('-' * 30)
escolha = input('Escolha a operação: ')
if escolha in ['+', '-', '*', '/']:
    num1 = float(input('Digite um valor: '))
    num2 = float(input('Digite outro valor: '))
    if escolha == '+':
        print(f'Resultado: {num1 + num2}')
    elif escolha == '-':
        print(f'Resultado: {num1 - num2}')
    elif escolha == '*':
        print(f'Resultado: {num1 * num2}')
    elif escolha == '/':
        if num2 != 0:
            print(f'Resultado: {num1 / num2}')
        else:
            print('Erro: Divisão por zero!')
    else: 
        print('Operação inválida!')