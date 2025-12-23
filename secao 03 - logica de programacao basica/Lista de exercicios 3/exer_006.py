"""
Exercicio 006
Faca um programa que imprima na tela os numeros
de 1 a 20, um abaixo do outro. Depois modifique
o programa para que ele mostre os numeros um ao
lado do outro.
"""

for numero in range(1, 21):
    print(numero)

for numero in range(1, 21):
    print(f'{numero} ', end='')
