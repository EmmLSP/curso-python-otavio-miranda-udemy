"""
Exercicio 001
Faca um programa que mostre na tela uma contagem
regressiva para o estouro de fogos de artificio,
indo de 10 ate 0, com uma pausa de 1 segundo
entre eles.
"""

from time import sleep
from random import randint

for c in range(10, -1, -1):
    r = randint(1, 6)
    print(f'\033[1;3{r}m{c}\033[m')
    sleep(0.5)
sleep(0.5)
print('BUM! BUM! POOOW!')
