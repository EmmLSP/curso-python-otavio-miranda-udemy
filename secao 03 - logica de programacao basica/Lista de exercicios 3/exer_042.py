"""
Exercicio 042
Faca um programa que leia uma quantidade indeterminada de 
numeros positivos e conte quantos deles estao nos seguintes 
intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada
de dados devera terminar quando for lido um numero negativo.
"""

from time import sleep
from os import system

intervalo_25 = intervalo_50 = intervalo_75 = intervalo_100 = 0
numeros = ''
while True:
    num = int(input('Digite um numero ou digite num < 0 para sair: '))

    if num > 100:
        print('Numero precisa ser entre 0 e 100')
        continue
   
    if  num < 0:
        print('Encerrando...')
        sleep(1)
        break
    
    if 0 <= num <= 25:
        intervalo_25 += 1
    elif 25 < num <= 50:
        intervalo_50 += 1
    elif 50 < num <= 75:
        intervalo_75 += 1
    else:
        intervalo_100 += 1
    numeros += f'{num} '

system('cls')
print('-' * 30)
if num == ' ':
    print('Nenhum numero foi digitado')
else:
    print(f'Numeros digitados: {numeros}')
    print(f"Estao no intervalo de [000-025] = {intervalo_25} numeros")
    print(f"Estao no intervalo de [026-050] = {intervalo_50} numeros")
    print(f"Estao no intervalo de [051-075] = {intervalo_75} numeros")
    print(f"Estao no intervalo de [076-100] = {intervalo_100} numeros")
