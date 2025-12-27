"""
Exercicio 007
Faca um programa que leia um numero inteiro
e diga se ele e ou nao um numero primo.
"""

# v1
num = int(input('Digite um numero: '))
primo = 0
for c in range(1, num+1):
    if num % c == 0:
        print(f'\033[1;33m{c}\033[m ', end='')
        primo += 1
    else:
        print(f'\033[1;31m{c}\033[m ', end='')
print()

print(f'O numero {num} foi divisivel {primo} vezes')
if primo == 2:
    print('É um numero PRIMO!')
else:
    print('E por isso ele NAO é PRIMO!')
print()

# v2
num = int(input('Digite um numero: '))
primo = True
if num < 2:
    primo = False
for c in range(2, num):
    if num % c == 0:
        primo = False
        break
if primo:
    print(f'O {num} é um numero PRIMO!')
else:
    print(f'O {num} NAO é um numero PRIMO!')
