"""
Exercicio 022
Faca um programa que mostre a tabuada de varios
numeros, um de cada vez, para cada valor digitado
pelo usuario. O programa sera interrompido quando
o numero solicitado for negativo.
"""

from time import sleep

while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        print(f'\nFinalizando programa...')
        print('-' * 20)
        sleep(1.5)
        break
    print(f'\nTabuada do {num}:')
    print('-' * 20)
    for c in range(1, 11):
        print(f'{num} x {c:2} = {num*c}')
        sleep(0.5)
    print('-' * 20, '\n')

print('PROGRAMA TABUADA ENCERRADO! Volte sempre!')
