"""
Exercicio 036
Desenvolva um programa que faca a tabuada de um
numero qualquer inteiro que sera digitado pelo
usuario, mas a tabuada nao deve necessariamente
iniciar em 1 e terminar em 10, o valor inicial e
final devem ser informados tambem pelo usuario,
conforme exemplo abaixo:

Montar a tabuada de: 5
Comecar por: 4
Terminar em: 7

Vou montar a tabuada de 5 comecando em 4 e terminando em 7:
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
"""

from time import sleep
from random import randint

num = int(input('Digite um numero para a tabuada: '))

while True:
    num_inicial = int(input('Digite o inicio da tabuada: '))
    num_final = int(input('Digite o final da tabuada: '))
    if num_inicial > num_final:
        print('Numero final menor do que o numero inicial')
        continue
    break

print('Gerando tabuada...')
sleep(1)

print(f'Montar a tabuada de: {num}')
print(f'Comecar por: {num_inicial}')
print(f'Terminar em: {num_final}')

print(f'\033[\033[32mVou montar a tabuada do \033[m{num} ', end='')
print(f'\033[32mcomecando em \033[m{num_inicial}\033[32m e terminando em \033[m{num_final}:')

for n in range(num_inicial, num_final+1):
    c = randint(1, 5)
    print(f'\033[{c+30}m{num} x {n:2} = {num*n}\033[m')
    sleep(0.5)
