"""
Exercicio 19
Faca um programa que peca um numero inteiro e 
determine se ele é par ou impar.
"""

numero = int(input('Digite um numero: '))
par_impar = False
if numero % 2 == 0:
    par_impar = True
if par_impar:
    print(f'{numero} é PAR')
else:
    print(f'{numero} é ÍMPAR')
