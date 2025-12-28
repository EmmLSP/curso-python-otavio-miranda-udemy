"""
Exercicio 018
Escreva um programa que leia um numero n inteiro
qualquer e mostre na tela os n primeiros elementos
de uma sequencia de Fibonacci.

Ex.: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
"""

print('-' * 40)
print(f'{'Sequencia de Fibonacci':^40}')
print('-' * 40)

num = int(input('Quantos termos voce quer mostrar: '))
primeiro = 0
segundo = 1
c = 2
# numeros a partir de 3
print('~' * 40)
print(f'{primeiro} -> {segundo} -> ', end='')
while c < num:
    terceiro = primeiro + segundo
    primeiro = segundo
    segundo = terceiro
    print(f'{terceiro}', end='')
    print(' -> ' if c < num - 1 else ' -> FIM\n', end='')
    c += 1
print('~' * 40)
