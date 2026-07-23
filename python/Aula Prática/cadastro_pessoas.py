#Uso de IA para melhorar o código e facilitar o entendimento geral...

def menu(): 
    print('-----Gerenciamento de Pessoas-----') 
    print('----------------------------------') 
    print('[1]Cadastrar') 
    print('[2]Listar') 
    print('[3]Remover') 
    print('[4]Sair') 
    print('----------------------------------') 

def valida_int(pergunta, min, max): 
    x = int(input(pergunta)) 
    while((x < min) or (x > max)): 
        x = int(input(pergunta)) 
    return x 

def existeArquivo(nArquivo): 
    try: 
        a = open(nArquivo, 'rt') # Abrindo para leitura 
        a.close() 
    except FileNotFoundError: 
        return False 
    else: 
        return True # CORRIGIDO: Retorna True se o arquivo existir

def criarArquivo(nArquivo): 
    try: 
        a = open(nArquivo, 'wt+') 
        a.close() 
    except: 
        print('Erro ao criar arquivo.') 
    else: 
        print(f'Arquivo {nArquivo} criado com sucesso! \n') 

def cadastrar(x, y): 
    try: 
        a = open(x, 'at', encoding='utf-8') # Encoding adicionado para evitar erros com acentos
    except: 
        print('Erro ao cadastrar.') 
    else: 
        a.write(f'{y}\n') 
        print('Nome cadastrado com sucesso!') 
    finally: 
        a.close() 

def listar(x): 
    try: 
        a = open(x, 'rt', encoding='utf-8') 
    except: 
        print('Erro ao ler arquivo') 
    else: 
        print(a.read()) 
    finally: 
        a.close() 

def remover(x, nome): 
    try: 
        # Versão simplificada usando o gerenciador 'with'
        with open(x, 'r', encoding='utf-8') as a: 
            linhas = a.readlines() 
            
        linhas_filtradas = [l for l in linhas if l.strip() != nome] 
        
        with open(x, 'w', encoding='utf-8') as a: 
            a.writelines(linhas_filtradas) 
            
        print(f"Nome '{nome}' removido com sucesso!") 
    except FileNotFoundError: 
        print('Erro: O arquivo não foi encontrado.') 
    except Exception as e: 
        print(f'Ocorreu um erro inesperado: {e}') 

# Programa Principal 
arquivo = 'lista_de_pessoas.txt' 

if existeArquivo(arquivo): 
    print('Arquivo localizado no computador.') 
else: 
    print('Arquivo inexistente.') 
    criarArquivo(arquivo) # CORRIGIDO: Agora só cria se não existir (evita limpar o arquivo existente)

while True: 
    menu() 
    op = valida_int('>> ', 1, 4) 
    
    if (op == 1): 
        print('OPÇÃO DE CADASTRO SELECIONADA') 
        nome = input('Digite o nome da pessoa: ') 
        cadastrar(arquivo, nome) 
        
    if (op == 2): 
        print('OPÇÃO DE LISTAR SELECIONADA') 
        listar(arquivo) 
        
    if (op == 3): 
        print('OPÇÃO DE REMOVER SELECIONADA') 
        pessoa = input('Digite o nome da Pessoa a ser removida >> \n') 
        remover(arquivo, pessoa) 
        
    if (op == 4): 
        print('Encerrando o programa . . .') 
        break
