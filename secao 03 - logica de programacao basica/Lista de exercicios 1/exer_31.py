"""
Exercicio 31
Faca um programa que leia um numero de
0 a 9999 e mostre na tela cada um dos
digitos separados.

Ex: 
Digite um numero: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1
"""

numero_str = input('Informe um numero: ')
numero = int(numero_str)
print(f'Analizando o numero {numero}')
if len(numero_str) == 4:
    print('-' * 25)
    print(f'Unidade: {numero_str[3]}')
    print(f'Dezena: {numero_str[2]}')
    print(f'Centena: {numero_str[1]}')
    print(f'Milhar: {numero_str[0]}')
print('-' * 25)
unidade = numero // 1 % 10
dezena =  numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')
print('-' * 25)
