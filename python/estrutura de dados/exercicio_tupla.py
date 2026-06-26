palavras = ('Mario', 'Luigi', 'Peach', 'Yoshi', 'Bowser')

for palavra in palavras: #Pega cada palavra
    print(f'\nPalavra: {palavra.upper()}. Vogais: ')
    for letra in palavra: #Pega a letra da palavra e mostra as vogais contidas
        if letra.lower() in 'aeiou': #Transformo todas letras em minúsculas para não dar erro
            print(letra.upper(), end=' ') #Volto com maiúsculas
