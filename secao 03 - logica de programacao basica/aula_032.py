# Exercícios 3, 4 e 5

"""
3. Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# opcao 1
try:
    entrada = input('Digite um numero: ')
    num = int(entrada)
    if num % 2 == 0:
        print(f'{num} é PAR')
    else:
        print(f'{num} é ÍMPAR')
except:
    print('Não não digitou um numero inteiro')

# opcao 2
entrada = input('Digite um numero: ')
# metodo de string para verificar se existem somente numeros
if entrada.isdigit():
    num = int(entrada)
    if num % 2 == 0:
        print(f'{num} é PAR')
    else:
        print(f'{num} é ÍMPAR')
else:
    print('Não não digitou um numero inteiro')

# opcao 3
entrada = input('Digite um numero: ')
if entrada.isdigit():
    entrada_int = int(entrada)
    # retorna uma boolean
    par_impar = entrada_int % 2 == 0
    # flag
    par_impar_text = 'IMPAR'
    if par_impar is True:
        par_impar_text = 'PAR'
    print(f'O numero {entrada_int} é {par_impar_text}')
else:
    print('Voce nao digitou um numero inteiro')

"""
4. Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# opcao 1
entrada = input('Digite a hora em numeros inteiros: ')
if entrada.isdigit():
    hora = int(entrada)
    if 0 <= hora <= 11:
        print('Bom Dia!')
    elif 12 <= hora <= 17:
        print('Boa Tarde!')
    elif 18 <= hora <= 23:
        print('Boa Noite!')
    else:
        print('Não conheco essa hora')
else:
    print('Por favor, digite um numero inteiro')

# opcao 2
entrada = input('Digite a hora em numeros inteiros: ')
try:
    hora = int(entrada)
    if hora >= 0 and hora <= 11:
        print('Bom Dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa Tarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa Noite!')
    else:
        print('Não conheco essa hora')
except:
    print('Por favor, digite um numero inteiro')


"""
5. Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".  
"""

# input() sempre retorna uma string

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)
# string com valor = is not None = True
# isalpha(), se for somente letras is True
if nome and nome.isalpha():
    if tamanho_nome > 1:
        print(f'Nome: {nome}')
        print(f'Tamanho nome: {tamanho_nome}')
        if tamanho_nome <= 4:
            print('Seu nome é curto')
        elif tamanho_nome >= 5 and tamanho_nome <= 6:
            print('Seu nome é normal')
        # nome > 6 letras
        else:
            print('Seu nome é muito grande')
    else: # String '' vazia = is None = False
        print('Digite mais de uma letra')
else:
    print('Por favor, digite um nome com letras')
