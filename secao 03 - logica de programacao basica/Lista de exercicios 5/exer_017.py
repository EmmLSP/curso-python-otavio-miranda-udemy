"""
Exercicio 017
Faca um programa que ajude um jogador da MEGA-SENA
a criar palpites. O programa vai perguntar quantos
jogos serao gerados e vai sortear 6 numeros entre 1
e 60 para cada jogo, cadastrando tudo em uma lista
composta.
"""

from random import randint
from time import sleep

print('-' * 30)
print(F'{'JOGA NA MEGA SENA':^30}')
print('-' * 30)

qtd_jogos = int(input('Quantos jogos voce quer que eu sortei? '))

jogos = list()
jogo = list()
for c in range(qtd_jogos):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont >= 6:
            break
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
print()

print('-=' * 5, f' SORTEANDO {qtd_jogos} JOGOS ', '-=' * 5)
for pos, jogo in enumerate(jogos):
    print(f'Jogo {pos + 1:2}: [', end='')
    for i, lista in enumerate(jogo):
        if i < len(jogo) - 1:
            print(f'{lista:02}, ', end='')
        else:
            print(f'{lista:02}]')
    sleep(1)
print()

print('-=' * 30)
print(f'{'LISTA COMPOSTA DOS JOGOS SORTEADOS...'}')
sleep(1)
print(jogos)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
