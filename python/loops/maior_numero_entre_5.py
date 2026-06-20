def logo():
    print('---------------------------')
    print('Ache o maior número entre 5')
    print('---------------------------')
    print('Começar (1)')
    print('Sair (2)')
logo()
while True: 
    op = int(input('Escolha a opção: '))
    if op == 1:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite um número: '))
        n3 = float(input('Digite um número: '))
        n4 = float(input('Digite um número: '))
        n5 = float(input('Digite um número: '))
        if n1 >= n2 and n1 >= n3 and n1 >= n4 and n1 >= n5:
            print(f'O maior número é {n1}')
            logo()
        else:
            if n2 >= n1 and n2 >= n3 and n2 >= n4 and n1 >= n5:
                print(f'O maior número é {n2}')
                logo()
            else: 
                if n3 >= n1 and n3 >= n2 and n3 >= n4 and n3 >= n5:
                    print(f'O maior número é {n3}')
                    logo()
                else:
                    if n4 >= n1 and n4 >= n2 and n4 >= n3 and n4 >= n5:
                        print(f'O maior número é {n4}')
                        logo()
                    else:
                        print(f'O maior número é {n5}')
                        logo()
    if op == 2 or op >= 3 or op <= 0:
        print('Encerrando programa...')
        break
3