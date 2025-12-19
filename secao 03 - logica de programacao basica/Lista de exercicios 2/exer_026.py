"""
Exercicio 026
Faca um programa que faca o computador pensar 
em um numero entre 0 e 5 e peca para o usuario 
tentardescobrir qual foi o numero escolhido pelo 
computador.
O programa devera escrever na tela se o usuario
venceu ou perdeu.
"""

from random import randint
from time import sleep

print('\033[33m-=-' * 20, '\033[m')
print(f'\033[34m{'Vou pensar em um numero entre 0 e 5. Tente adivinhar...':^60}\033[m')
print('\033[33m-=-' * 20, '\033[m')

computador = randint(0, 5)
jogador = int(input('Em que numero eu pesei? '))
print('\033[35mPROCESSANDO...\033[m')
sleep(1)

if jogador == computador:
    print(f'\033[32mParabens! Voce conseguiu me vencer!\033[m')
else:
    print(f'\033[31mGANHEI! Eu pensei no numero {computador} e nao no {jogador}!\033[m')
