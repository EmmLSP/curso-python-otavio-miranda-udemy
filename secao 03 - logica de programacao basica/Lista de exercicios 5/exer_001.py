"""
Exercicio 001
Crie um programa que tenha uma tupla totalmente
preenchida com uma contagem por extenso, do zero
ate vinte.

Seu programa devera ler um numero pelo teclado
(entre 0 e 20) e mostra-lo por extenso.
"""

from time import sleep
from os import system

contagem = ('zero', 'um', 'dois', 'tres', 'quatro',
    'cinco','seis','sete','oito','nove','dez', 
    'onze','doze','treze','catorze','quinze',
    'dezesseis','dezessete','dezoito','dezenove','vinte')

print('-' * 30)
while True:
    while True:
        numero = int(input('Digite um numero entre 0 e 20: '))
        if numero < 0 or numero > 20:
            print('Tente novamente. ', end='')
            continue
        break

    print(f'Voce digitou o numero {contagem[numero]}')

    while True:
        resp = input('Quer continuar? S/N ').upper().strip()[0]
        if resp in 'SN':
            break
        print('Entreada invalida! Digite \'S\' ou \'N\'')
    
    if resp == 'S':
        system('cls')
        print('-' * 30)
        continue
    
    if resp == 'N':
        system('cls')
        print('\nEncerrando programa...')
        sleep(1)
        break

print('-' * 30)
print('Fim do Programa! Volte Sempre!')
