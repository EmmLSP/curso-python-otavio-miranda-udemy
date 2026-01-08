"""
Exercicio 003
Crie um programa que vai gerar cinco numeros
aleatorios e colocar em uma tupla.
Depois disso, mostre a listagem de numeros
gerados e tambem indique o menor e o maior
valor que estao na tupla.
"""

from random import randint
from time import sleep

numeros = (
    randint(1, 10), randint(1, 10),
    randint(1, 10), randint(1, 10),
    randint(1, 10))

maior = menor = 0
for pos, num in enumerate(numeros):
    if pos == 0:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    
print(f'Os valores sorteados foram: ', end='')
for num in numeros:
    if num == maior:
        print(f'\033[1;32m{num}\033[m ', end='', flush=True)
    elif num == menor:
        print(f'\033[1;31m{num}\033[m ', end='', flush=True)
    else:
        print(f'\033[1;33m{num}\033[m ', end='', flush=True)
    sleep(0.5)
print()
print(f'O maior valor sorteado foi {maior}')
print(f'O maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {menor}')
print(f'O menor valor sorteado foi {min(numeros)}')
