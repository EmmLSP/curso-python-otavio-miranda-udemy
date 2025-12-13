"""
Exercicio 29
O mesmo professor do desafio anterior quer sortear a ordem de 
apresentação de trabalhos dos alunos. Faca um programa que leia 
o nome dos quatro alunos e mostre a ordem sorteada.
"""

from random import shuffle

aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos) # shuffle -> embaralhar
print('-' * 20)
print('A ordem de apresentação será:')
print('-' * 20)
print(f'1° aluno - {alunos[0]}')
print(f'2° aluno - {alunos[1]}')
print(f'3° aluno - {alunos[2]}')
print(f'4° aluno - {alunos[3]}')
print('-' * 20)
print(alunos)
print('-' * 20)
