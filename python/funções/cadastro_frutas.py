def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro ao criar arquivo.')
    else:
        print(f'Arquivo {nomeArquivo} criado com sucesso! \n')

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def cadastrarFruta(arquivo, nomeFruta):
    try:
        a = open(arquivo, 'at')
    except:
        print('Erro ao abrir o arquivo.')
    else:
        a.write(f'{nomeFruta} \n')
        print('Fruta cadastrada com sucesso!')
    finally:
        a.close()

def listarFruta(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler arquivo.')
    else:
        print(a.read())
    finally:
        a.close()

def menu():
    print('-' * 30)
    print('Menu')
    print('Cadastrar fruta [1]')
    print('Listar frutas [2]')
    print('Sair [3]')
    print('-' * 30)

#Programa principal
arquivo = 'Lista_de_frutas.txt'
if existeArquivo(arquivo): 
    print('Arquivo Localizado no computador.')
else:
    print('Arquivo inexistente.')
    criarArquivo(arquivo)

while True:
    menu()
    op = valida_int('Escolha a opção desejada: ', 1, 3)
    if (op == 1):
        print('Opção de cadastro selecionada')
        nomeFruta = input('Digite o nome da fruta: ')
        cadastrarFruta(arquivo, nomeFruta)
    if (op == 2):
        print('Opção de listar selecionada.')
        listarFruta(arquivo)
    if (op == 3):
        print('Encerrando o pograma . . .')
        break