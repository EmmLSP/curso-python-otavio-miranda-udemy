"""
Exercicio 05
Faca um programa que leia um numero inteiro e
mostre na tela o seu sucessor e antecessor.
"""

numero = input('Digite um numero: ')
print(type(numero))
numero_int = int(numero)
print(type(numero_int))
antec = numero_int - 1
suces = numero_int + 1
print(f'Analisando o valor {numero_int}, seu antecessor é {antec} e seu sucessor é {suces}')
