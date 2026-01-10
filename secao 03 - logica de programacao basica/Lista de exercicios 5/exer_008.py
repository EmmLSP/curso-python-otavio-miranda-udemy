"""
Exercicio 008
Crie um programa onde o usuario possa digitar
varios valores numericos e cadastre-os em uma
lista. Caso o numero ja exista la dentro, ele
nao sera adicionado.
No final, no final serao exibidos todos os 
valores unicos digitados, em ordem crescente.
"""

from time import sleep
from os import system

numeros = []
while True:
    num = int(input('Digite um valor: '))
    if num not in numeros:
        print(f'\033[32mValor adicionado com sucesso...\033[m')
        numeros.append(num)
    else:
        print(f'\033[31mValor duplicado! Não vou adicionar...\033[m')
    while True:
        resp = input('Quer continuar? [S/N]: ').strip().upper()[0]
        if resp in 'SN':
            break
        print('\033[33mEntrada invalida! Digite \'S\' ou \'N\'\033[m')
    if resp == 'N':
        system('cls')
        print('\n\033[34mEncerrando programa...\033[m')
        sleep(1.5)
        break

numeros.sort()
print('-=' * 30)
print(f'Voce digitou os valores {numeros}')
