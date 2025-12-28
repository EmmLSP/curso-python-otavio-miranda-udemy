"""
Exercicio 013
Melhore o jogo da Adivinhacao do Mundo 1 onde o cumputador
vai "pensar" em um numero entre 0 e 10. So que agora o 
jogador vai tentar adivinhar ate acertar, mostrando no final 
quantos palpites foram necessarios para vencer.
"""

from random import randint
from time import sleep

computador = randint(0, 10)
print('\033[33m-=-\033[m' * 20)
print(f'\033[34m{'Sou seu computador...':>27}\033[m')
print(f'\033[34m{'Acabei de pensar em num numero entre 0 e 10.':>50}\033[m')
print(f'\033[34m{'Sera que voce consegue adivinhar qual foi?':>48}\033[m')
print('\033[33m-=-\033[m' * 20)
palpites = 0
acertou = False
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    print('Processando...')
    sleep(0.5)
    if jogador > computador:
        print('Menos... Tente mais uma vez.')
    elif jogador < computador:
        print('Mais... Tente mais uma vez.')
    else:
        print(f'Voce Acertou! Eu pensei no numero {computador}.')
        sleep(1)
        acertou = True
    palpites += 1

print(f'Voce acertou com {palpites} tentativas. Parabens!')
