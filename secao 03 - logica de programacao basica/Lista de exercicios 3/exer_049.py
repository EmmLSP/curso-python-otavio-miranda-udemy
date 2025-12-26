"""
Exercicio 049
Faca um programa que mostre os n termos da serie
a seguir:
S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
"""

termos = int(input('Digite os n termos para formar uma serie n/m: '))
soma = 1
print('S = ', end='')
for n in range(1, termos+1):
    print(f'{n}/{soma} + ', end='')
    soma += 2
print('... + n/m.')
