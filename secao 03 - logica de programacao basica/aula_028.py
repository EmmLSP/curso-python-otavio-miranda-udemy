"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite o seu nome: ').strip()
idade = input('Digite sua idade: ')

# ' ' - True - 1
# '' - False - 0
# if 0 and 0 - False
# if 0 and 1 - False
# if 1 and 0 - False
# if 1 and 1 - True

# se nome ou idade estiverem vazias, o retorno da expressao vai ser False
if nome and idade:
    lista_string = nome.split()
    if len(lista_string) == 1:
        print(f'Seu nome é {lista_string[0]}')
        print(f'Seu nome invertido é {lista_string[0][::-1]}')
    if len(lista_string) > 1:
        print(f'Seu nome completo é {nome}')
        print(f'Seu nome completo invertido é {nome[::-1]}')
    if ' ' in nome:
        if nome.count(' ') == 1:
            if nome.count(' ') == 1:
                print(f'Seu nome contem {nome.count(' ')} espaco')
            else:
                print(f'Seu nome contem {nome.count(' ')} espaco')
        else:
            print(f'Seu nome contem {nome.count(' ')} espacos')
    else:
        print(f'Seu nome nao contem espacos')
    if ' ' not in nome:
        print(f'Seu nome sem espaco tem {len(''.join(lista_string))} letras')
    else:
        print(f'{len(''.join(lista_string))} letras + {nome.count(' ')} espaco = {len(nome)} caracteres')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
    # print(f'A ultima letra do seu nome é {nome[len(nome) - 1]}')
else:
    print('Desculpe, voce deixou campos vazios')
