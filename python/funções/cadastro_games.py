def menu():
    print('-' * 30)
    print('Menu')
    print('Cadastrar novo item [1]')
    print('Listar Cadastros [2]')
    print('Sair [3]')
    print('-' * 30)

def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def criarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+') #wt o arquivo vai ser criado e limpo, o + é atualização
        a.close()
    except:
        print('Erro na criação do arquivo.')
    else:
        print(f'Arquivo {nomeArquivo} criado com sucesso!\n')

def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo, 'at') #At usado para abrir o arquivo para escrita
    except:
        print('Erro ao abrir o arquivo.')
    else:
        a.write(f'{nomeJogo};{nomeVideogame} \n')
    finally:
        a.close() #Fechar o arquivo caso tenha outros erros...

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt') #Rt para leitura 
    except:
        print('Erro ao ler o arquivo.')
    else: #Se der tudo certo o else é executado
        print(a.read())
    finally:
        a.close()


#programa principal
arquivo = 'games.txt'
if existeArquivo(arquivo): #ExisteArquivo except retorna falso então executa a criação do arquivo, caso já exista é printado a linha abaixo. . .
    print('Arquivo localizado no computador.')
else:
    print('Arquivo inexistente')
    criarArquivo(arquivo) #Chama a função para criar o arquivo

while True:
    menu()
    op = valida_int('Escolha a opção desejada: ', 1, 3)
    if (op == 1): #Novo item
        print("Opção de cadastrar novo item selecionada . . . \n")
        nomeJogo = input('Nome do jogo: ')
        nomeVideogame = input('Nome do videogame: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)

    elif (op == 2): #Listar
        print("Opção de listar selecionada . . . \n")
        listarArquivo(arquivo)
    elif (op == 3):
        print('Encerrando . . .')
        break