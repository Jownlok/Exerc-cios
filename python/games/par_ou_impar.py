from random import randint #Importanto a biblioteca random para gerar números aleatórios

def menu():
    print('-' * 30)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('[1] PAR')
    print('[2] ÍMPAR')
    print('[3] Sair')
    print('-' * 30)

while True:
    menu()

    escolha = int(input('Escolha uma opção: '))

    if escolha == 1:
        jogador_tipo = 'PAR'
    elif escolha == 2:
        jogador_tipo = 'ÍMPAR'  
    elif escolha == 3:
        print('Saindo do jogo...')
        break
    else:
        print('Opção inválida. Tente novamente.')
        continue

    jogador = int(input('Digite um número: '))
    computador = randint(0, 10) #O Computador pega um número aleatório entre 0 e 10

    total = jogador + computador

    resultado = 'PAR' if total % 2 == 0 else 'ÍMPAR' #Resultado é PAR se o total for divisível por 2, caso contrário é ÍMPAR

    print(f'Você jogou {jogador} e o computador jogou {computador}.')
    print(f'Total de {total} deu {resultado}.')

    if jogador_tipo == resultado:
        print('Você VENCEU!')
    else:
        print('Você PERDEU!')
        break