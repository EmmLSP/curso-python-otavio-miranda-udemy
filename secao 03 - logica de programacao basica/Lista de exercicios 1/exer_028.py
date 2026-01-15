"""
Exercicio 28
Um professor quer sortear um de seus quatro alunos para
apagar o quadro. Faca um programa que ajude ele, lendo o
nome deles e escrevendo o nome escolhido.
"""

from random import choice

nome1 = input('Primeiro nome: ')
nome2 = input('Segundo nome: ')
nome3 = input('Terceiro nome: ')
nome4 = input('Quarto nome: ')
alunos = [nome1, nome2, nome3, nome4]
escolhido = choice(alunos)
print(f'O aluno escolhido foi {escolhido}')
