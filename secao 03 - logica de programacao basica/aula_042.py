# while - Qual letra apareceu mais vezes na frase? (Iterando strings com while)

frase = 'O Python é uma linguagem de programação'\
    'multipardigma. ' \
    'Python foi criado por Guido Von Rossum.'.lower()

print(frase.count('python')) # 2x

frase = 'O Python é uma linguagem de programação'\
    'multipardigma. ' \
    'Python foi criado por Guido Von Rossum.'.upper()

print(frase.count('PYTHON')) # 2x

frase = 'O Python é uma linguagem de programação'\
    'multiparadigma.\n' \
    'Python foi criado por Guido Van Rossum.'

print(frase)
print(frase.count('Python')) # 2x

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
letras = ''
while i < len(frase):
    letra_atual = frase[i]
    if letra_atual != ' ':
        qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)
    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual
    i += 1

print('-' * 15)
print(f'A letra que apareceu mais vezes foi \'{letra_apareceu_mais_vezes}\' que apareceu {qtd_apareceu_mais_vezes}x')

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
letras = ''
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)
    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual
    i += 1

print('-' * 15)
print(f'A letra que apareceu mais vezes foi \'{letra_apareceu_mais_vezes}\' que apareceu {qtd_apareceu_mais_vezes}x')
