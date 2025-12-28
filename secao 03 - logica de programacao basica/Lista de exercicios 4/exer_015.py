"""
Exercicio 015
Faca um programa que leia um numero qualquer
e mostre o seu fatorial.

Exercício Python #060 - Cálculo do Fatorial
"""

from time import sleep
from os import system

# v1 - versao com while
sair = False
while not sair:
    num = int(input('Digite um numero para calcular seu fatorial: '))
    if num < 2:
        print(f'{num}! = 1')
        print('-' * 20)
        continue
    fat = 1
    c = num
    print(f'Calculando {num}! = ', end='')
    while c > 0:
        fat *= c
        print(f'{c}', end='')
        print(' x ' if c > 1 else ' = ', end='')
        c -= 1
    print(fat)
    print('-' * 20)
    
    encerrar = False
    while not encerrar:
        resp = input('Quer continuar? [S/N] ').upper().strip()
        if resp == 'S' or resp == 'N':
            encerrar = True

    if resp == 'N':
        print('Encerrando...')
        sleep(1)
        sair = True

print('Fim do Programa! Volte sempre!')
sleep(3)

system('cls')

# v2 - versao com for
sair = False
while not sair:
    num = int(input('Digite um numero para calcular seu fatorial: '))
    if num < 2:
        print(f'Calculando {num}! = 1')
        print('-' * 20)
        continue
    fat = 1
    print(f'Calculando {num}! = ', end='')
    for c in range(num, 0, -1):
        fat *= c
        print(f'{c}', end='')
        print(' x ' if c > 1 else ' = ', end='')
    print(fat)
    print('-' * 20)
    
    encerrar = False
    while not encerrar:
        resp = input('Quer continuar? [S/N] ').upper().strip()
        if resp == 'S' or resp == 'N':
            encerrar = True
    
    if resp == 'N':
        print('Encerrando...')
        sleep(1)
        sair = True

print('Fim do Programa! Volte sempre!')
