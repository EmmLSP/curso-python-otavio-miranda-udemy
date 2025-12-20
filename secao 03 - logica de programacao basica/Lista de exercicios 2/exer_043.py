"""
Exercicio 043
Faca um programa que faca o programa jogar
jokenpo com voce.

Regras do jogo:
pedra - papel - tesoura
- pedra ganha de tesoura e perde de papel
- papel ganha de pedra e perde de tesoura
- tesoura ganha de papel e perde de pedra
"""

from random import randint
from time import sleep

computador = randint(0, 2)
itens = ('PEDRA', 'PAPEL', 'TESOURA') # tupla
print('-' * 20)
print('''Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
print('-' * 20)
jogador = int(input('Qual é a sua jogada: '))
if jogador == 0 or jogador == 1 or jogador == 2:
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!!!')
    print('-=' * 12)
    print(f'Computador jogou {itens[computador]}')
    print(f'Jogador jogou {itens[jogador]}')
    print('-=' * 12)
    if computador == 0: # computador jogou pedra
        if jogador == 0: # jogador jogou pedra
            print('EMPATE')
        elif jogador == 1: # jogador jogou papel
            print('COMPUTADOR VENCE')
        elif jogador == 2: # jogador jogou tesoura
            print('COMPUTADOR VENCE')
    elif computador == 1: # computador jogou papel
        if jogador == 0: # jogador jogou pedra
            print('COMPUTADOR VENCE')
        elif jogador == 1: # jogador jogou papel
            print('EMPATE')
        elif jogador == 2: # jogador jogou tesoura
            print('JOGADOR VENCE')
    elif computador == 2: # computador jogou tesoura
        if jogador == 0: # jogador jogou pedra
            print('JOGADOR VENCE')
        elif jogador == 1: # jogador jogou papel
            print('COMPUTADOR VENCE')
        elif jogador == 2: # jogador jogou tesoura
            print('EMPATE')
else:
    print('JOGADA INVALIDA!')
