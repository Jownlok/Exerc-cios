from num2words import num2words

def menu():
    print('-' * 30)
    print('MENU PRINCIPAL')
    print('[1] Converter data para string')
    print('[2] Sair')
    print('-' * 30)

def converter(dia, mes, ano):
    dia_extenso = num2words(dia, lang='pt_BR')
    mes_extenso = num2words(mes, lang='pt_BR')
    ano_extenso = num2words(ano, lang='pt_BR')

    return(f'Data: {dia_extenso} de {mes_extenso} de {ano_extenso}')

while True:
    menu()
    op = int(input('Escolha uma opção: '))
    if op == 1:
        dia = int(input('Digite o dia: '))
        mes = int(input('Digite o mês: '))
        ano = int(input('Digite o ano: '))
        resultado = converter(dia, mes, ano)
        print(resultado)

    elif op == 2:
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida. Tente novamente.')
