"""
Exercicio 002
Faca um programa que peca um valor e mostre na
tela se o valor é positivo ou negativo.
"""

entrada = input('Digite um valor: ')
if entrada.isdigit():
    num = int(entrada)
    if num >= 0:
        print(f'{entrada} é POSITIVO')
    else:
        print(f'{entrada} é NEGATIVO')
else:
    print('Não é um numero')
