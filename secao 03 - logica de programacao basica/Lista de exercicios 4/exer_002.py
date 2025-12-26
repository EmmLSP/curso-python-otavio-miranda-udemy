"""
Exercicio 002
Crie um programa que mostre na tela todos os
numeros pares que estao no intervalo entre 
1 e 50.
"""

from time import sleep
from random import randint

print('Todos os numeros pares no intervalo entre 1 e 50 v1')
for c in range(2, 51, 2):
    r = randint(1, 5)
    print(f'\033[1;3{r}m{c}\033[m ', end='', flush=True)
    sleep(0.5)
print('Acabou')

print('Todos os numeros pares no intervalo entre 1 e 50 v2')
for c in range(2, 51):
    r = randint(1, 5)
    if c % 2 == 0:
        print(f'\033[1;3{r}m{c}\033[m ', end='', flush=True)
        sleep(0.5)
print('Acabou')
