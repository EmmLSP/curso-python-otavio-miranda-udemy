"""
Exercicio 25
Crie um programa que leia um numero real qualquer pelo
teclado e mostre na tela a sua porção inteira.

Ex: Digite um numero: 6.127
O numero digitado 6.127 tem a parte inteira 6.
"""

from math import trunc, floor

# ceil - arrendonda para cima
# floor - arredonda para baixo
# trunc - corta parte inteira do numero
# int() - converte de float para int

num_str = input('Digite um valor: ')
num = float(num_str)
print(f'O valor digitado foi {num} e a sua porção inteira é {int(num)}')
print(f'O valor digitado foi {num} e a sua porção inteira é {trunc(num)}')
print(f'O valor digitado foi {num} e a sua porção inteira é {floor(num)}')
