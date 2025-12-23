"""
Exercicio 012
Desenvolva um gerador de tabuada, capaz de gerar a tabuada 
de qualquer numero entre 1 e 10. O usuario deve informar de 
qual numero ele deseja ver a tabuada. A saida deve ser 
conforme o exemplo abaixo:

Tabuada de 5:
-------------
5 x  1 = 5
5 x  2 = 10
...
5 x 10 = 50 
-------------
"""

from time import sleep
from os import system

pontilhados = '-' * 13

while True:

    num = int(input('Digite um numero para ver a tabuada entre 1 e 10: '))

    if num < 0 or num > 10:
        print('Entrada invalida! Digite um numero no intervalo entre 1 e 10')
        continue
    
    print(f'Tabuada de {num}:')
    sleep(0.5)

    print(pontilhados)
    for n in range(1, 11):
        print(f'{num} x {n:2} = {num*n}')
        sleep(0.5)
    print(pontilhados)

    while True:
        resp = input('Quer continuar? S/N ').upper()
        if resp in 'SN':
            if resp == 'S':
                system('cls')
            break
        print('Entrada invalida! Digite \'S\' ou \'N\'')
    
    if resp == 'N':
        print('ENCERRANDO...')
        sleep(1)
        break

print(pontilhados)
print('<<< FIM DO PROGRAMA >>>')
