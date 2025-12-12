"""
Exercicio 07
Faca um programa que peca 4 notas bimestrais e
mostre a media.
"""

nota1_str = input('Primeira nota do aluno: ')
nota2_str = input('Segunda nota do aluno: ')
nota3_str = input('Terceira nota do aluno: ')
nota4_str = input('Quarta nota do aluno: ')
nota1 = float(nota1_str)
nota2 = float(nota2_str)
nota3 = float(nota3_str)
nota4 = float(nota1_str)
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f'A media entre {nota1:.1f}, {nota2:.1f}, {nota3:.1f} e {nota4:.1f} é igual a {media:.1f}')
