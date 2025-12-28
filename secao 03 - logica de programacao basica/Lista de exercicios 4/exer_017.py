"""
Exercicio 017
Melhore o DESAFIO 016, perguntando para o usuario
se ele quer mostrar mais alguns termos. O programa
encerra quando ele disser que quer mostrar 0 termos.
"""

from time import sleep

print('Gerador de PA')
print('-=' * 15)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termos = 10
c = 0
sair = False
while not sair:
    while c < termos:
        print(primeiro, end='')
        print(' -> ' if c < termos - 1 else ' -> PAUSA\n', end='')
        primeiro += razao
        c += 1
    mais = int(input('Quantos termos voce quer mostrar mais? '))
    termos += mais
    if mais == 0:
        print('Finalizando...')
        sleep(1)
        sair = True

print(f'Progressao finalizanda com {termos} termos mostrados.')
