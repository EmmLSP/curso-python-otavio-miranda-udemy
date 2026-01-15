"""
Exercicio 27
Faca um programa que leia um angulo qualquer e mostre na 
tela o valor do seno, cosseno e tangente desse angulo.
"""

from math import sin, cos, tan, radians

angulo_str = input('Digite o angulo que voce deseja: ')
angulo = float(angulo_str)
seno = sin(radians(angulo))
cose = cos(radians(angulo))
tang = tan(radians(angulo))
print(f'O angulo de {angulo} tem o SENO de {seno:.2f}')
print(f'O angulo de {angulo} tem o COSSENO de {cose:.2f}')
print(f'O angulo de {angulo} tem o TANGENTE de {tang:.2f}')
