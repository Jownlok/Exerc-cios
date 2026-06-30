def menu():
    print('-' * 30)
    print('(Gerenciamento de Pessoas)')
    print('(1) Cadastrar')
    print('(2) Listar')
    print('(3) Sair')
    print('-' * 30)

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
        print(f'Arquivo {nomeArquivo} criado com sucesso!')


def cadastrarPessoas(arquivo, nomeArquivo, Idade):
    try:
        a = open(arquivo, 'at')
    except:
        print('Erro ao abrir o arquivo.')
    else:
        a.write(f'{nomeArquivo}, {Idade}\n')
        print('Pessoa cadastrada com sucesso!')
    finally:
        a.close()

def listarPessoas(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao abrir arquivo.')
    else:
        print(a.read())
    finally:
        a.close()

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while (x < min) or (x > max):
          x = int(input(pergunta))
    return x

#Programa Principal
arquivo = 'lista_de_pessoas.txt'
if existeArquivo(arquivo):
    print('Arquivo encontrado!')
else:
    print('Arquivo inexistente.')
    criarArquivo(arquivo)

while True:
    menu()
    op = valida_int('Escolha a opção desejada: ', 1, 3)
    if (op == 1):
        print('Opção de Cadastrar selecionada.')
        nomeArquivo = input('Digite o nome: ')
        Idade = input('Digite a idade: ')
        cadastrarPessoas(arquivo, nomeArquivo, Idade)
    if (op == 2):
        print('Opção de Listar selecionada.')
        listarPessoas(arquivo)
    if (op == 3):
        print('Encerrando o programa. . .')
        break