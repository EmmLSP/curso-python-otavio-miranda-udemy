"""
Exercicio 014
Crie um programa que leia dois valores e mostre um
menu na tela:

[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NUMEROS
[ 5 ] SAIR DO PROGRAMA

Seu programa devera realizar a operacao solicitada
em cada caso.
"""

from time import sleep
from os import system

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))

menu_opcoes = 'MENU DE OPCOES:\n' \
'[ 1 ] SOMAR\n' \
'[ 2 ] MULTIPLICAR\n' \
'[ 3 ] MAIOR\n' \
'[ 4 ] NOVOS NUMEROS\n' \
'[ 5 ] SAIR DO PROGRAMA'

sair = False 
while not sair:
    print(menu_opcoes)
    opcao = int(input('Qual é a sua opcao? '))
    if opcao != 5:
        system('cls')
    if opcao == 1:
        print(f'A soma entre {num1} + {num2} é {num1 + num2}')
    elif opcao == 2:
        print(f'O resultado de {num1} x {num2} é {num1 * num2}')
    elif opcao == 3:
        if num1 > num2:
            print(f'Entre {num1} e {num2} o valor maior é {num1}')
        elif num2 > num1:
            print(f'Entre {num1} e {num2} o valor maior é {num2}')
        else:
            print(f'Os dois numeros sao iguais')
    elif opcao == 4:
        print('-=' * 15)
        print('Informe os numeros novamente:')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
        system('cls')
        print(f'Novos Numeros: {num1=}, {num2=}')
    elif opcao == 5:
        print('\nFinalizando...')
        sair = True
    else:
        system('cls')    
        print('Opcao invalida! Tente novamente')
        print('-=' * 15)
        sleep(1)
        continue
    print('-=' * 15)
    sleep(1)

print('Fim do Programa! Volte sempre!')
