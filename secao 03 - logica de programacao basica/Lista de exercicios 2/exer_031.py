"""
Exercicio 031
Faca um programa que leia tres numeros e
mostre qual é maior e qual é menor.
"""

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

menor = n1
if n2 <= n1 and n2 <= n3:
    menor = n2
if n3 <= n1 and n3 <= n2:
    menor = n3

maior = n1
if n2 >= n1 and n2 >= n3:
    maior = n2
if n3 >= n1 and n3 >= n2:
    maior = n3

print(f'[{n1}, {n2}, {n3}]')
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')

if n1 >= n2 and n1 >= n3:
    maior = n1
elif n2 >= n1 and n2 >= n3:
    maior = n2
else:
    maior = n3

if n1 <= n2 and n1 <= n3:
    menor = n1
elif n2 <= n1 and n2 <= n3:
    menor = n2
else:
    menor = n3

print(f'[{n1}, {n2}, {n3}]')
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')

if n1 >= n2 and n1 >= n3:
    maior = n1
    if n2 < n3:
        menor = n2
    else:
        menor = n3
elif n2 >= n1 and n2 >= n3:
    maior = n2
    if n1 < n3:
        menor = n1
    else:
        menor = n3
else:
    maior = n3
    if n1 < n2:
        menor = n1
    else:
        menor = n2

print(f'[{n1}, {n2}, {n3}]')
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')
