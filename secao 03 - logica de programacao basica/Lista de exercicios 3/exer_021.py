"""
Exercicio 021
Faca um prorgrama que peca um numero inteiro e
determine se ele é ou nao um numero primo. Um
numero primo é aquele que é divisivel somente
por ele mesmo e por 1.
"""

num = int(input('Digite um numero: '))

primo = 0
for n in range(1, num+1):
    if num % n == 0:
        primo += 1

if primo == 2:
    print(f'{num} é PRIMO')
else:
    print(f'{num} NÃO é PRIMO')

num = int(input('Digite um numero: '))

primo = True
for n in range(2, num):
    if n % 2 == 0:
        print(n)
        primo = False
        break

if primo is True:
    print(f'{num} é PRIMO')
else:
    print(f'{num} NÃO é PRIMO')
