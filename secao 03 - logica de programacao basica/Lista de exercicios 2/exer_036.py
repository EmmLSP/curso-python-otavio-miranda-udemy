"""
Exercicio 036
Escreva um programa que leia dois numeros inteiros
e compare-os, mostrando na tela uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois sao iguais
"""

num1 = int(input('Primeiro numero: '))
num2 = int(input('Segundo numero: '))
maior_valor = ''
if num1 > num2:
    maior_valor = 'O PRIMEIRO valor é maior'
elif num2 > num1:
    maior_valor = 'O SEGUNDO valor é maior'
else:
    maior_valor = 'Não existe valor maior, os dois sao iguais'
print(maior_valor)
