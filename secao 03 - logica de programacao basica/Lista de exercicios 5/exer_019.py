"""
Exercicio 019 
Faca um programa que leia nome e media
de um aluno, guardando tambem a situacao
em um dicionario. No final, mostre o 
conteudo da estrutura na tela.
"""

aluno = {}
aluno['Nome'] = input('Nome: ')
aluno['Media'] = float(input(f'Media de {aluno['Nome']}: '))
if aluno['Media'] >= 7:
    aluno['Situacao'] = 'Aprovado'
elif aluno['Media'] >= 5:
    aluno['Situacao'] = 'Recuperacao'
else:
    aluno['Situacao'] = 'Reprovado'

print('-=' * 30)
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')
