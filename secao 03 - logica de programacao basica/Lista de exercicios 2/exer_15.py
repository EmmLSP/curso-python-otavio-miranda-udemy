"""
Exercicio 15
Faca um programa que calcule as raizes de uma equacao do segundo 
grau, na forma ax² + bx + c. O programa devera pedir os valores de 
a, b e c e fazer as consistencias, informando ao usuario 
nas seguintes situacoes:

a. Se o usuario informar o valor de A igual a zero, a equacao nao e 
do segundo grau e o programa nao deve pedir os demais
valores, sendo encerrado.
b. Se o delta calculado for negativo, a equacao nao possui raizes 
reais. Informe ao usuario e encerre o programa.
c. Se o delta calculado for igual a zero a equacao possui apenas uma
reaiz real, informe ao usuario.
d. Se o delta for positivo, a equacao possui duas raizes reais,
informe ao usuario.
"""

from math import sqrt

a = float(input('Digite o valor de a: '))
if a == 0:
    print('A igual a zero, nao é equacao do 2 grau')
else:
    b = float(input('Digite o valor de b: '))
    c = float(input('Digite o valor de c: '))
    delta = (b ** 2) - (4 * a * c)
    print(f'Delta: {delta}')
    if delta < 0:
        print('Delta negativo, equacao do 2 grau nao possui raizes reais')
    else:
        raiz_1 = (- b + (sqrt(delta))) / (2 * a)
        raiz_2 = (- b - (sqrt(delta))) / (2 * a)
        print(f'Raiz 1: {raiz_1:.2f}')
        print(f'Raiz 2: {raiz_2:.2f}')
        if delta == 0:
            print('A equacao do 2 grau possui apenas uma raiz real')
        else:
            print('A equacao do 2 grau possui duas raizes reais')
