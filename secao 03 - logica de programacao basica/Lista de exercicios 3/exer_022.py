"""
Exercicio 022
Altere o programa de calculo dos numeros primos,
informando, caso o numero nao seja primo, por 
quais numeros ele é divisivel.
"""

num = int(input('Digite um numero: '))

primo = True

if num < 2:
    primo = False

for n in range(2, num):
    if num % n == 0:
        primo = False
        break

if not primo:
    print(f'{num} NAO é PRIMO')
    if num > 1:
        for n in range(1, num+1):
            if num % n == 0:
                print(f'{num} é divisivel por {n}')
else:
    print(f'{num} é PRIMO')
    for n in range(1, num+1):
        if num % n == 0:
            print(f'{num} é divisivel por {n}')
